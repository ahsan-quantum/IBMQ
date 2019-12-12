#########################################################################
#------------------------------------------------------------------------
# This code was used to generate probability distribution of errors
# in [[7, 1, 3]] encoded qubit using measurement statistics obtained
# from experiments executed on IBMQ_16_melbourne device. The details of
# relevant experiments can be found in the corresponding research paper
# available: https://github.com/ahsan-quantum/IBMQ/blob/master/ForIBM.pdf
#-----------------------------------------------------------------------
#########################################################################

from numpy import matrix
from itertools import combinations as comb
from copy import deepcopy


def update_dic_steane(dic1):
                                        # The function maps 7-bits long classical bit-string
                                        # to steane codewords w/wo errors 
                                        # Define Steane Stabilizers
    test_deed = [[1,0,1,0,1,0,1],\     
                 [0,1,1,0,0,1,1],\
                 [0,0,0,1,1,1,1],\
                 [1,1,0,1,0,0,1],\
                 [1,1,0,0,1,1,0],\
                 [0,1,1,1,1,0,0],\
                 [1,0,1,1,0,1,0]];

    
    dic1_val_sum = 0
    tar_dic_val_sum = 0
    tar_dic = {}    
    for bin_str in dic1:        # iterate over measurement outcomes contained in classical measurement results 
        val = dic1[bin_str]
        x_b_v = []
        len_x_b_v = 0
        for j in bin_str:
            if j == '0':
                x_b_v.append(0)
            else:
                x_b_v.append(1)
                len_x_b_v += 1
    
        if len_x_b_v > 2:
            min_len = len_x_b_v
            min_len_seq = x_b_v
            
            for test_seq in test_deed:
                test_seq_mat = matrix(test_seq)
                res = test_seq_mat ^ matrix(x_b_v)
                res = res.tolist()[0]
                if sum(res) < min_len:
                    min_len_seq = res
                    min_len = sum(res)
            min_str = ''
            for bit in min_len_seq:
                min_str = min_str + str(bit)
                            
            if tar_dic.get(min_str) == None:
                tar_dic[min_str] = val
            else:
                tar_dic[min_str]+= val

        else:

            if tar_dic.get(bin_str) == None:
                tar_dic[bin_str] = val
            else:
                tar_dic[bin_str]+= val
            

        dic1_val_sum += val
    return tar_dic

def reverse_dic_keys(dic1,nbits,hex_not_bin=True):   # Unlike Qiskit, we like to work with big-endian format
                                                     # The function converts measurement outcome dictionary keys into
                                                     # big-endian format.
    tar_dic = {}    
    for hex_str in dic1:
        #-----------First convert Hex to Bin----------
        if hex_not_bin:
            bin_str = bin(int(hex_str,16))[2:].zfill(nbits)
        else:
            bin_str = hex_str
        #----------Generate iterator of reversed bit-string---------
        rev_bin_str_iter = reversed(bin_str)

        rev_bin_str = ''
        for i in range(nbits):
            rev_bin_str += rev_bin_str_iter.__next__()
        
        tar_dic[rev_bin_str] = dic1[hex_str]

    return tar_dic



def err_count(dic1,nbits):              # Returns a dictionary whose keys indicate number of qubits in error
                                        # and corresponding values contain statistics/8192 (e.g. '101':321)
    err_dic = {}    
    err_dic = err_dic.fromkeys(range(nbits+1),0)  

    for bin_str in dic1:                 
        err_count = 0
        for j in bin_str:
            if j == '1':
                err_count += 1
        
        err_dic[err_count]+= dic1[bin_str]
    return err_dic

def measure_steane_syndrome(v):
                                        # Returns error Steane 3-qubit error syndrome as string
    Stabilizer = [[1,0,1,0,1,0,1],\
                  [0,1,1,0,0,1,1],\
                  [0,0,0,1,1,1,1]]

    res_str = ''
    for stab in Stabilizer:
        res = 0
        for i in range(len(stab)):
            if stab[i] * v[i] == 1:
                res += 1

        res = res%2
        res_str += str(res)

    return res_str

def gen_cosyndrome_dics(dic1):      # Returns three dictionaries, each mapping error count to syndromes.

    single_err = {}                 # Dictionary for single-qubit error syndrome
    double_err = {}                 # Dictionary for two-qubit error syndrome
    logical_err = {}                # Dictionary for three-qubit error syndrome
                        
    for bin_str in dic1:                  
        val = dic1[bin_str]
        x_b_v = []
        for j in bin_str:
            if j == '0':
                x_b_v.append(0)
            else:
                x_b_v.append(1)
                
        res_str = measure_steane_syndrome(x_b_v)
        dicto = {}
        if sum(x_b_v)==1:       # Single-qubit error
            dicto = single_err
        elif sum(x_b_v)==2:     # Two-qubit errors 
            dicto = double_err
        elif sum(x_b_v)==3:     # Three-qubits (Logical error)
            dicto = logical_err

        if dicto.get(res_str) == None:
            dicto[res_str] = val
        else:
            dicto[res_str] += val
        
    return [single_err,double_err,logical_err]

def compute_fail_prob_lowest(dic1, dic2): # Calculates total failure probability according to eq (5) of the paper
    sum1 = 0
    for key in dic1:
        if not dic2.get(key) == None:
            sum1 += min(dic1[key],dic2[key])
    return sum1

def correlations(dic1,nbits):  # Calculates Pearson correlation matrix for seven encoding qubits

    comb_list = list(comb(range(nbits),2))
    comb_list.append((0,0))
    comb_list.append((1,1))
    comb_list.append((2,2))
    comb_list.append((3,3))
    comb_list.append((4,4))
    comb_list.append((5,5))
    comb_list.append((6,6))

    print(comb_list)
    #---------------First Calculate probabilities---------------
    p_xy_11 = [[0 for i in range(nbits)] for j in range(nbits)]
    p_xy_10 = [[0 for i in range(nbits)] for j in range(nbits)]
    p_xy_01 = [[0 for i in range(nbits)] for j in range(nbits)]
    p_xy_00 = [[0 for i in range(nbits)] for j in range(nbits)]

    p_x_1 = [0 for i in range(nbits)]
    p_x_0 = [0 for i in range(nbits)]

    
    for bin_str in dic1:
        
        val = dic1[bin_str]
        x_b_v = []
        index = 0
        for j in bin_str:
            if j == '1':
                p_x_1[index] += val/8192.0
                x_b_v.append(1)
            else:
                p_x_0[index] += val/8192.0
                x_b_v.append(0)

            index += 1

        for k in comb_list:
            x = k[0]
            y = k[1]
            if x_b_v[x] == 1 and x_b_v[y] == 1:
                p_xy_11[x][y] += val/8192.0
                p_xy_11[y][x] += val/8192.0
            elif x_b_v[x] == 1 and x_b_v[y] == 0:
                p_xy_10[x][y] += val/8192.0
                p_xy_10[y][x] += val/8192.0
            elif x_b_v[x] == 0 and x_b_v[y] == 1:
                p_xy_01[x][y] += val/8192.0
                p_xy_01[y][x] += val/8192.0
            else: 
                p_xy_00[x][y] += val/8192.0
                p_xy_00[y][x] += val/8192.0

            
    #print (p_xy_11,p_xy_01,p_xy_10,p_xy_00)
    #-----------Now calculate Expectations, Std---------------
    E_x = [0 for i in range(nbits)]
    Std_x = [0 for i in range(nbits)]
    
    E_xy = [[0 for i in range(nbits)] for j in range(nbits)]

    for i in range(nbits):
        E_x[i] = p_x_1[i] - p_x_0[i]
        E_x_2 = (p_x_1[i] + p_x_0[i])

        Std_x[i] = (E_x_2 - E_x[i]**2)**0.5
        
        for j in range(i+1,nbits):
            E_xy[i][j] =  p_xy_11[i][j] -  p_xy_10[i][j] -  p_xy_01[i][j] +  p_xy_00[i][j]
            E_xy[j][i] =  p_xy_11[i][j] -  p_xy_10[i][j] -  p_xy_01[i][j] +  p_xy_00[i][j]
    #----------------Finally calculate correlations------
    
    corr_mat = [[0 for i in range(nbits)] for j in range(nbits)]
    for i in range(nbits):
        for j in range(nbits):
            corr_mat[i][j] = (E_xy[i][j]-E_x[i]*E_x[j])/(Std_x[i]*Std_x[j])
            corr_mat[j][i] = (E_xy[j][i]-E_x[j]*E_x[i])/(Std_x[j]*Std_x[i])

    return corr_mat


#---------Sample Experimental data---------------------
dic1 = {'0011001': 4, '1000110': 5, '0101000': 33, '0111001': 1, '0100011': 5, '0010011': 12, '0110000': 19, '1001100': 3, '1000100': 14, '1000010': 25, '0010101': 1, '0001000': 540, '1011010': 1, '0001110': 30, '0011000': 74, '0000000': 3564, '0000001': 350, '0000110': 110, '0011111': 1, '0000101': 9, '0010001': 31, '1001010': 9, '0000111': 9, '0101100': 4, '0001011': 25, '0001100': 57, '0000010': 1671, '0111010': 2, '0011011': 2, '0001010': 295, '1111101': 1, '0100100': 10, '1100010': 1, '0100110': 6, '0110100': 2, '0111000': 5, '1101001': 1, '0100010': 72, '0011010': 35, '0010110': 11, '1001000': 9, '0011100': 9, '1110010': 1, '1010010': 3, '0000011': 158, '0101010': 16, '0110001': 3, '1100100': 1, '1000000': 29, '0110010': 6, '1011101': 1, '0001101': 2, '0100000': 168, '1001110': 1, '0001111': 1, '1011000': 1, '1000111': 1, '0010010': 145, '1101000': 1, '0101110': 1, '0011110': 8, '1010000': 5, '0101011': 3, '1001001': 1, '0010100': 14, '1000011': 4, '0000100': 183, '0100001': 7, '0001001': 41, '1000001': 1, '0110011': 3, '0010000': 315}

tar_dic = reverse_dic_keys(dic1,7,False)
tar_dic = update_dic_steane(tar_dic)
[S,D,L] = gen_cosyndrome_dics(tar_dic)


print(S)
print(D)
print(L)

err_dic = err_count(tar_dic,7)
print (err_dic)

print('total failure prob. High Weight')  
print((compute_fail_prob_lowest(S, D)+ min(err_dic[0],err_dic[3]))/8192.0)

print('total failure prob. Low Weight') # Calculates total failure probability according to eq (5) of the paper
print((err_dic[2]+ min(err_dic[0],err_dic[3]))/8192.0)

print ('---------------------')


