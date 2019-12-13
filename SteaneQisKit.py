#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ                                                                                                           
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
IBMQ.enable_account('0e7f14b28f85776f07155dc21f882ec678239c0d42d3e8cb8bf2ea0827f49ce31d1d593f8a66a1d2f356166d1191fb841f64adc1566c7da48b35488e83411a86') 
#IBMQ.load_accounts()


# In[4]:


0


# In[3]:


from qiskit import IBMQ
# IBMQ.load_account()

# backend = provider.get_backend('ibmq_16_melbourne')
# backend = provider.get_backend('ibmq_london')
print("Available backends:")
 
IBMQ.backends() 
from qiskit.providers.ibmq import least_busy 

large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= 7 and 
                                                       not x.configuration().simulator) 
 
print(large_enough_devices) 
#backend = large_enough_devices[6] 
backend = least_busy(large_enough_devices) 
print("The best backend is " + backend.name()) 


# In[4]:


print(large_enough_devices[0])


# In[20]:





# In[5]:


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute

N = 14
C = 7

qr = QuantumRegister(N)
cr = ClassicalRegister(C)
circuit = QuantumCircuit(qr, cr)

#---------Qubit Map-----------
#P = {1:2, 2:11, 3:12, 4:4, 5:1, 6:10, 7:3}    # (4,5)...
P = {1:9, 2:4, 3:5, 4:11, 5:8, 6:3, 7:10}    # (4,5) ainvee/nahee yaar it is cool...
# P = {1:8, 2:10, 3:7, 4:5, 5:6, 6:4, 7:9}     # v.cool (2,3)...
#P = {1:4, 2:2, 3:1, 4:11, 5:10, 6:12, 7:3}   # ainvee (1,3)...
# P = {1:3, 2:12, 3:11, 4:1, 5:0, 6:13, 7:2}   # looks okay(1,5).....
# P = {1:9, 2:11, 3:8, 4:4, 5:5, 6:3, 7:10}    # looks okay(2,3)...
# P = {1:4, 2:2, 3:5, 4:11, 5:10, 6:12, 7:3}   # fazool (2,3)
#P = {1:2, 2:4, 3:1, 4:11, 5:12, 6:10, 7:3}   # just ok (2,3)...
#P = {1:8, 2:10, 3:11, 4:5, 5:6, 6:4, 7:9}   # darmayana (1,3)....
P = {1:9, 2:4, 3:5, 4:11, 5:12, 6:3, 7:10}  # (1,5) cool/ver cool...

# P = {1:13, 2:2, 3:1, 4:11, 5:10, 6:3, 7:12}  # not bad (1,5)...
# P = {1:11, 2:2, 3:3, 4:13, 5:10, 6:1, 7:12}  # not bad (4,5)...
#P = {1:11, 2:4, 3:3, 4:9, 5:8, 6:5, 7:10}  #  not bad (1,5)...
# P = {1:4, 2:9, 3:5, 4:11, 5:3, 6:12, 7:10}  # cool (2,6)......

#P = {1:4, 2:2, 3:1, 4:11, 5:10, 6:12, 7:3}  # darmayana (1,3) : fazool waale ka variant
#P = {1:3, 2:12, 3:11, 4:1, 5:4, 6:13, 7:2}   # (4,5) variant of looks okay(1,5).....
#P = {1:2, 2:4, 3:5, 4:11, 5:12, 6:10, 7:3}   # variant of just ok just ok (1,3)...
#P = {1:4, 2:6, 3:3, 4:9, 5:10, 6:8, 7:5}   # (2,3)
# P = {1:4, 2:9, 3:5, 4:11, 5:3, 6:8, 7:10}  # cool (4,6)......
#dummy_qbt = 13  # must not be in P values and initialized to |0> state
#-------Nov 2019---Direct |+> state prep-----
# P = {1:11, 2:2, 3:9, 4:12, 5:4, 6:3, 7:10} #vv bad
# P = {1:10, 2:3, 3:4, 4:12, 5:13, 6:2, 7:11}
# P = {1:3, 2:10, 3:4, 4:12, 5:2, 6:9, 7:11} # missing CNOT (6,4) 
#----------------------
circuit.h(qr[P[1]])
circuit.h(qr[P[2]])
circuit.h(qr[P[4]])
#----------------------------------------
# circuit.h(qr[P[7]])
# circuit.h(qr[P[6]])
# circuit.h(qr[P[5]])
# circuit.h(qr[P[3]])
#----------Do First--------(1,5)---
# circuit.cx(qr[P[1]],qr[P[7]])
# circuit.cx(qr[P[7]],qr[P[4]])
# circuit.cx(qr[P[4]],qr[P[5]])
# circuit.cx(qr[P[5]],qr[P[4]])
# circuit.cx(qr[P[1]],qr[P[7]])
# #-----------------------------
# circuit.reset(qr[P[2]])
# circuit.reset(qr[P[6]])
# circuit.reset(qr[P[3]])

# circuit.h(qr[P[2]])
# circuit.h(qr[P[4]])
# [(2,6),(4,6),(2,3),(1,3),(2,7),(4,7),(7,1),(1,7),(5,4),(4,5),(7,4)]
# circuit.h(qr[P[1]])
# circuit.h(qr[P[2]])
# circuit.h(qr[P[4]])
# circuit.h(qr[P[3]])
# circuit.h(qr[P[5]])
# circuit.h(qr[P[6]])
# circuit.h(qr[P[7]])
#vooter = 0
#if randint(0,1)==1:
#    vooter = 1

#circuit.h(qr[P[5]])

# CNOT_lst = [(4,6),(2,6),(2,3),(1,3),(1,7),(2,7),(4,7)]#,(4,5),(1,5)]
#CNOT_lst = [(1,7),(2,7),(4,7),(4,5),(1,5),(4,6),(2,6),(2,3),(1,3)]
#CNOT_lst = [(1,7),(2,7),(4,7),(4,6),(2,6),(4,5),(1,5),(1,3),(2,3)]
#CNOT_lst = [(4,6),(2,6),(2,3),(1,3),(1,7),(2,7),(4,7),(1,5),(4,5)]
#CNOT_lst = [(2,3),(1,3),(1,7),(2,7),(4,7),(1,5),(4,5),(4,6),(2,6)]
#-------------control oriented---------
# CNOT_lst = [(2,7),(2,6),(2,3),(1,3),(1,5),(1,7),(4,7),(4,6)]#,(4,5)]
#CNOT_lst = [(2,3),(2,6),(2,7),(4,7),(4,6),(4,5),(1,3),(1,7),(1,5)]
#CNOT_lst = [(2,7),(2,3),(2,6),(4,6),(4,7),(4,5),(1,5),(1,7),(1,3)]
#CNOT_lst = [(4,6),(4,7),(4,5),(1,5),(1,3),(1,7),(2,7),(2,6),(2,3)]
#CNOT_lst = [(1,3),(1,7),(4,7),(1,5),(4,5),(4,6),(2,7),(2,3),(2,6)]

#---------Nov --------------
# CNOT_lst = [(1,7),(3,7),(5,7),(5,6),(2,6),(1,6),(1,4),(2,4),(3,4)] ###-nahee yaar
# CNOT_lst = [(7,4),(6,4),(5,4),(7,2),(6,2),(3,1),(3,2),(7,1),(5,1)]

CNOT_lst = [(2,6),(4,6),(2,3),(1,3),(2,7),(4,7),(7,1),(1,7),(5,4),(4,5),(7,4)]
# CNOT_lst = [(2,7),(1,3),(2,3),(4,6),(2,6),(4,7),(7,1),(4,5),(1,7),(5,4),(7,4)]
# CNOT_lst = [(1,5),(2,6),(2,3),(1,3),(2,7),(4,7),(7,1),(1,7),(5,4),(4,5),(7,4)]
# CNOT_lst = [(2,3),(1,3),(1,7),(4,7),(4,5),(1,5),(6,4),(4,6),(7,2),(2,7),(7,4)]
# CNOT_lst = [(4,6),(2,6),(4,7),(1,5),(4,5),(1,7),(3,1),(1,3),(7,2),(2,7),(7,1)] 
# CNOT_lst = [(4,6),(2,6),(4,5),(1,5),(4,7),(1,7),(3,1),(1,3),(7,2),(2,7),(7,1)]
# CNOT_lst = [(2,3),(1,3),(1,5),(4,5),(1,7),(2,7),(6,2),(2,6),(7,4),(4,7),(7,2)]
# CNOT_lst = [(2,3),(1,3),(4,5),(1,5),(4,7),(1,7),(6,4),(7,2),(4,6),(2,7),(7,4)]
# CNOT_lst = [(5,1),(3,1),(7,1),(5,4),(3,2),(7,2),(4,7),(7,4),(2,6),(6,2),(2,7)]
# CNOT_lst = [(1,7),(4,7),(2,6),(4,6),(1,5),(4,5),(7,2),(3,1),(2,7),(1,3),(7,1)]
# CNOT_lst = [(2,6),(4,6),(1,3),(2,3),(4,7),(2,7),(5,4),(4,5),(7,1),(1,7),(7,4)]

Missing_CNOT = [11, 51]

ct = 0
for pair in CNOT_lst:
    a = pair[0]
    b = pair[1]
    if a != Missing_CNOT[0] or b != Missing_CNOT[1]:
        circuit.cx(qr[P[a]],qr[P[b]])
#     if ct == 4:
#         circuit.x(qr[P[7]])
#     circuit.z(qr)
#     ct += 1

# circuit.h(qr[P[5]])
# P = {1:9, 2:4, 3:5, 4:11, 5:12, 6:3, 7:10}  # (1,5) cool/ver cool...
##########
# P = {1:4, 2:8, 3:5, 4:10, 5:3, 6:9, 7:11} 
P = {1:10, 2:4, 3:5, 4:12, 5:11, 6:3, 7:9} 
# P = {1:4, 2:10, 3:5, 4:12, 5:3, 6:11, 7:9}

# P = {1:3, 2:10, 3:4, 4:12, 5:2, 6:9, 7:11}
# P = {1:3, 2:9, 3:4, 4:11, 5:2, 6:10, 7:12}

#P = {1:5, 2:3, 3:4, 4:11, 5:10, 6:12, 7:2} # fazool walay waala

# P = {1:10, 2:4, 3:5, 4:8, 5:11, 6:3, 7:9}  

for i in P:
    circuit.h(qr[P[i]])

# for i in P:
#     circuit.z(qr[P[i]])

# for i in range(30):
#     circuit.iden(qr)
#     circuit.barrier(qr)

from random import randint
#if rand()
Stab_dic  = [[1,0,1,0,1,0,1],             [0,1,1,0,0,1,1],             [0,0,0,1,1,1,1],             [1,1,1,0,0,0,0]];

for jj in range(1):
    for i in range(4):
        if randint(0,1)==1:
            Stab = Stab_dic[i]
            for j in range(7):
                if Stab[j]==1:
                    circuit.x(qr[P[j+1]])
        else:
            circuit.iden(qr)

    circuit.barrier(qr)

# for i in P:
#     circuit.z(qr[P[i]])


for i in P:
    circuit.h(qr[P[i]])

# if vooter == 1:
#     circuit.x(qr[P[5]])
#-----------New P------------
# P = {1:4, 2:10, 3:5, 4:12, 5:3, 6:11, 7:9} 
# P = {1:10, 2:4, 3:5, 4:12, 5:11, 6:3, 7:9} 
# P = {1:7, 2:9, 3:8, 4:5, 5:6, 6:4, 7:10}  
# P = {1:5, 2:3, 3:4, 4:11, 5:10, 6:12, 7:2} 

ct = 0
for i in P:
    circuit.measure(qr[P[i]],cr[ct])
    ct += 1


# In[42]:


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute
from copy import deepcopy
import random
N = 14   
C = 7

# V1 =    [13,  10,  12,  5,  4,  9,  0] 
# V2 =    [ 1,  11,   2,  6,  3,  8,  7] 

V1  =   [0,   12,   11,    4,  5,  8,   6] 
V2  =   [1,    2,    3,   10,  9,  7,  13]  

V1  =  [1,  11,  2, 10,  9,  8,   6]
V2  =  [0,  12,  3, 4,  5,  7,  13]

V1  =   [1,   12,   11,   5,   9,  8,  6] 
V2  =   [0,    2,   3,    4,  10,  7,  13]


# V1 =    [13,  11,   9,  5,  2,  6,  0] 
# V2 =    [ 1,  12,  10,  4,  3,  8,  7] 

# V1  =   [13,  2,  11,  5,  6,  7,  12] 
# V2  =   [ 1,  3,  10,  4,  9,  8,   0] 

# V1 =     [1, 13, 2, 5, 11,  9,   6] 
# V2 =     [0, 12, 3, 4, 10,  8,  13]

#V1 =     [1, 13,  2, 5, 11, 9,   6]
#V2 =     [0, 12,  3, 4, 10, 8,  11]
        
# V1 =     [0,2,13,10,5,6,9]         
# V2 =     [1,3,12,11,4,8,8]         

# V1 =     [8,5, 9,4,12,13,2]
# V2 =     [7,6,10,3,11, 1,1]

#V1 =     [8,5, 9,4,12,13,2]
# #V2 =     [7,6,10,3,11, 1,1]
# V1 = [13, 12, 10, 5, 4, 9, 0]
# V2 = [ 1,  2, 11, 6, 3, 8, 7]

# V1 = [8,  9, 12 ,13,2,4,6]     #M: 5da1e5c5595a0c00188f49a4
# V2 = [7, 10, 11 , 1,3,5,0] 

#V1 = [13, 12, 4, 10, 5, 6, 0]
#V2 = [ 1,  2, 3, 11, 9, 8, 7]
#V1 = [13, 12,  11, 4, 5, 6, 0]
#V2 = [ 1,  2,  10, 3, 9, 8, 7]
#V1 =     [0,2,13,10,5,6,9]
#V2 =     [1,3,12,11,4,8,7]

# V1   =    [13,2,0,10,5,9,6]
# V2   =    [12,3,1,11,4,8,7]

#V1 =     [1,11,4, 9,5,7,13] 
#V2 =     [2,12,3,10,6,8, 0]
# V1 =     [1,4,5, 9,11,7,13]  
# V2 =     [2,3,6,10,12,8, 0]
# V1 =     [13,7, 9,11,1,4,5]  
# V2 =     [ 0,8,10,12,2,3,6]
# V1 =     [8,5, 9,4,12,13,2]  #M: 5da1dddbecbd6d0018d9a16f
# V2 =     [7,6,10,3,11, 1,0]
num_ckt = 2
circuit_lst = []
for ckt_ct in range(num_ckt):
    qr = QuantumRegister(N)
    cr = ClassicalRegister(C)
    circuit = QuantumCircuit(qr, cr)
    # #--------both operand flipped------
    # # circuit.x(qr)
    # #--------bit-flipped either control or control ------
    circuit.h(qr)
    #-------swap 0,1-------
    # #--------phase-flipped either control or control ------
#     circuit.z(qr)
    # circuit.z(qr)
    # circuit.z(qr[V1[6]])
    for i in range(7):
        circuit.z(qr[V2[i]])
    #---------only for optimization----------
    for i in range(6):
        circuit.x(qr[V2[i]])

    # #circuit.x(qr)
    for i in range(6):
        circuit.cx(qr[V1[i]],qr[V2[i]])

    # for i in range(6):
    #    circuit.x(qr[V2[i]])

    # for i in range(6):
    #     circuit.cx(qr[V2[i]],qr[V1[i]])
    # circuit.swap(qr[1],qr[0])
    # circuit.cx(qr[13],qr[1])

    #------------(both operands flipped------------
    # circuit.z(qr)   # when target is measured
    # circuit.z(qr[V1[6]]) # when control is measured

    # #----------undro flipped control or target---------
#     for i in range(6):
#          circuit.z(qr[V1[i]])
    circuit.z(qr)
    circuit.z(qr[V1[6]])
    circuit.h(qr)

    # #-----Measure---------

    #circuit.x(qr[V1[6]])
#     for i in range(6):
#         circuit.x(qr[V1[i]])
    ct = 0
#     random.shuffle(V1)
    #V1.reverse()
    #print(V1)
    if ckt_ct > 0:
        Zampa = V1
    else:
        Zampa = V2
    #Zampa.reverse()
    for i in Zampa:
        circuit.measure(qr[i], cr[ct])
        ct += 1
        
    print(Zampa)

    circuit_lst.append(deepcopy(circuit))

#----------Hm-------
# circuit.measure(qr[V2[6]], cr[ct])

# #############################################
# #############################################
# N = 14
# C = 3 
# qr1 = QuantumRegister(N)
# cr1 = ClassicalRegister(C)

# V1 = [ 11,10, 9]
# V2 = [ 3, 4, 5]
# # des = 1
# # delay = 10
# ##########---Circuit-1---##########
# circuit1 = QuantumCircuit(qr1, cr1)
# #----------Encode [[3,1,3]]--------
# circuit1.h(qr1[V1[1]])
# # circuit1.h(qr1[V1[2]])
# circuit1.cx(qr1[V1[1]],qr1[V1[0]])
# circuit1.cx(qr1[V1[1]],qr1[V1[2]])

# circuit1.h(qr1[V2[1]])
# # circuit1.h(qr1[V2[2]])
# circuit1.cx(qr1[V2[1]],qr1[V2[0]])
# circuit1.cx(qr1[V2[1]],qr1[V2[2]])

# #-------Apply swap--------
# for i in range(3):
#     circuit1.cx(qr1[V2[i]],qr1[V1[i]])
# # for i in range(3):
# #     circuit1.cx(qr1[V1[i]],qr1[V2[i]])
# # for i in range(3):
# #     circuit1.cx(qr1[V2[i]],qr1[V1[i]])
# #-------------------------------
# #-----------Decode--------------
# circuit1.cx(qr1[V1[1]],qr1[V1[0]])
# circuit1.cx(qr1[V1[1]],qr1[V1[2]])
# circuit1.h(qr1[V1[1]])
# # circuit1.h(qr1[V1[0]])

# #-----Measure---------
# ct = 0
# for i in V1:
#     circuit1.measure(qr1[i], cr1[ct])
#     ct += 1
# #############------circuit-2--------############
# # #############################################
# N = 14
# C = 3 
# qr2 = QuantumRegister(N)
# cr2 = ClassicalRegister(C)

# # des = 1
# # delay = 10
# ##########---Circuit-2---##########
# circuit2 = QuantumCircuit(qr2, cr2)
# #----------Encode [[3,1,3]]--------
# # circuit2.h(qr2[V1[0]])
# circuit2.h(qr2[V1[1]])
# circuit2.cx(qr2[V1[1]],qr2[V1[0]])
# circuit2.cx(qr2[V1[1]],qr2[V1[2]])

# circuit2.h(qr2[V2[1]])
# # circuit2.h(qr2[V2[2]])
# circuit2.cx(qr2[V2[1]],qr2[V2[0]])
# circuit2.cx(qr2[V2[1]],qr2[V2[2]])

# #-------Apply swap--------
# for i in range(3):
#     circuit2.cx(qr2[V2[i]],qr2[V1[i]])
# # for i in range(3):
# #     circuit2.cx(qr2[V1[i]],qr2[V2[i]])
# # for i in range(3):
# #     circuit2.cx(qr2[V2[i]],qr2[V1[i]])
# #-------------------------------
# #-----------Decode--------------
# circuit2.cx(qr2[V2[1]],qr2[V2[0]])
# circuit2.cx(qr2[V2[1]],qr2[V2[2]])
# circuit2.h(qr2[V2[1]])
# # circuit2.h(qr2[V2[0]])

# #-----Measure---------
# ct = 0
# for i in V2:
#     circuit2.measure(qr2[i], cr2[ct])
#     ct += 1

# #     ##################################
# #     ##################################


# In[15]:


N = 14
C = 3 
qr1 = QuantumRegister(N)
cr1 = ClassicalRegister(C)
V1 = [10,  3,  9]
V2 = [ 4,  11, 5]
# des = 1
# delay = 10
##########---Circuit-1---##########
circuit1 = QuantumCircuit(qr1, cr1)

circuit1.h(qr1[V1[0]])
circuit1.h(qr1[V1[1]])
circuit1.h(qr1[V1[2]])

circuit1.h(qr1[V2[0]])
circuit1.h(qr1[V2[1]])
circuit1.h(qr1[V2[2]])

#-------Apply CNOT--------
for i in range(3):
    circuit1.cx(qr1[V2[i]],qr1[V1[i]])
# for i in range(3):
#     circuit1.cx(qr1[V1[i]],qr1[V1[i]])
# for i in range(3):
#     circuit1.cx(qr1[V2[i]],qr1[V1[i]])
#-------------------------------
circuit1.h(qr1[V1[0]])
circuit1.h(qr1[V1[1]])
circuit1.h(qr1[V1[2]])
#-----Measure---------
ct = 0
for i in V1:
    circuit1.measure(qr1[i], cr1[ct])
    ct += 1
#############------circuit-2--------############
# #############################################
N = 14
C = 3 
qr2 = QuantumRegister(N)
cr2 = ClassicalRegister(C)

# des = 1
# delay = 10
##########---Circuit-2---##########
circuit2 = QuantumCircuit(qr2, cr2)
#----------Encode [[3,1,3]]--------
circuit2.h(qr2[V1[0]])
circuit2.h(qr2[V1[2]])
circuit2.h(qr2[V1[1]])

circuit2.h(qr2[V2[0]])
circuit2.h(qr2[V2[2]])
circuit2.h(qr2[V2[1]])

#-------Apply CNOT--------
circuit2.cx(qr2[V2[0]],qr2[V1[0]])
circuit2.cx(qr2[V2[1]],qr2[V1[1]])
circuit2.cx(qr2[V2[2]],qr2[V1[2]])
#-------------------------------
circuit2.h(qr2[V2[0]])
circuit2.h(qr2[V2[2]])
circuit2.h(qr2[V2[1]])
#-----Measure---------
ct = 0
for i in V2:
    circuit2.measure(qr2[i], cr2[ct])
    ct += 1

    ##################################
    ##################################


# In[43]:


from qiskit import BasicAer
backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(circuit_lst[1], backend_sim, shots=1024)
result_sim = job_sim.result()
counts = result_sim.get_counts(circuit_lst[1])
print(counts)


# In[ ]:


shots = 8192          # Number of shots to run the program (experiment); maximum is 8192 shots.
max_credits = 3        # Maximum number of credits to spend on executions.
# circuit_lst = [circuit]
job_exp = execute(circuit_lst, backend=backend, shots=shots, max_credits=max_credits)
jobID = job_exp.job_id()
print('JOB ID: {}'.format(jobID))
result_exp = job_exp.result()
counts  = result_exp.get_counts(0)
print(counts)
# counts  = result_exp.get_counts(1)
# print(counts)


# In[38]:


job_exp=backend.retrieve_job('5debe41d3ccc1e0013b0ff61')
result_exp = job_exp.result() 
dic1 = result_exp.get_counts(1) 
print(dic1)
# dic1 = result_exp.get_counts(3) 
# print(dic1)


# In[9]:


from qiskit import execute, Aer, QuantumRegister
from qiskit.ignis.mitigation.measurement import (complete_meas_cal, tensored_meas_cal,
                                                 CompleteMeasFitter, TensoredMeasFitter)
from qiskit.providers.aer import noise
#qubit_list = [0,1,2,3,4,5,6]
#qr = qiskit.QuantumRegister(14)
qr = QuantumRegister(14)
#qubit_list = P.values()
#qubit_list = [4, 9, 5, 11, 3, 12, 10]  # cool (2,6)......

#P = {1:9, 2:4, 3:5, 4:11, 5:12, 6:3, 7:10}  #5d819dc9efa6b100189d3af9  
#P = {1:2, 2:11, 3:12, 4:4, 5:1, 6:10, 7:3}   #5d81bcd245d55500185f17f6     (4,5)
#P = {1:4, 2:9, 3:5, 4:11, 5:3, 6:12, 7:10}  #5d81c7c045d55500185f1832
#P = {1:8, 2:10, 3:7, 4:5, 5:6, 6:4, 7:9}    #5d81d22e9f1ddc0018b5117c   (2,3)
#P = {1:9, 2:4, 3:5, 4:11, 5:8, 6:3, 7:10}   #5d81e099596522001821aaf7    (1,5)
#P = {1:11, 2:4, 3:3, 4:9, 5:8, 6:5, 7:10}   #5d81f09645d55500185f18f5 
#P = {1:11, 2:2, 3:3, 4:13, 5:10, 6:1, 7:12} #5d81faca45d55500185f1927
#P = {1:8, 2:10, 3:11, 4:5, 5:6, 6:4, 7:9}   #5d8208f645d55500185f197d 
#P = {1:13, 2:2, 3:1, 4:11, 5:10, 6:3, 7:12} #5d8209262e977a0018e41006 
#P = {1:9, 2:11, 3:8, 4:4, 5:5, 6:3, 7:10}   #5d8233e69f1ddc0018b51391 
#P = {1:3, 2:12, 3:11, 4:1, 5:0, 6:13, 7:2}  #5d823f2e2e977a0018e4114c
#P = {1:4, 2:2, 3:1, 4:11, 5:10, 6:12, 7:3}  #5d82539507fdea0018980391 
#P = {1:2, 2:4, 3:1, 4:11, 5:12, 6:10, 7:3}  #5d826156ff7d8300184cf6ea 
#P = {1:4, 2:2, 3:5, 4:11, 5:10, 6:12, 7:3}  #5d8280022e977a0018e412dd 

#P = {1:4, 2:2, 3:1, 4:11, 5:10, 6:12, 7:3} 
P = {1:3, 2:9, 3:4, 4:11, 5:2, 6:10, 7:12}
#--`-``-------`+
 
#P = {1:4, 2:9, 3:5, 4:11, 5:3, 6:12, 7:10}
#Actual_qbt_lst = [P[i] for i in range(1,8)]
#Actual_qbt_lst = [13,12,2, 4,5,6,0]
#Actual_qbt_lst = [13,12,4,10,5,6,0]
#Actual_qbt_lst = [13, 12, 2, 5,  4,  9, 0]

# P = {1:4, 2:8, 3:5, 4:10, 5:3, 6:9, 7:11} 
# Actual_qbt_lst = [P[i] for i in range(1,8)]
# Actual_qbt_lst =     [0,2,13,10,5,6,9]   
Actual_qbt_lst  =   [0,   12,   10,   4,  9,  8,  6] 
# Actual_qbt_lst =  [ 1, 2,11,6,3,8,7]
meas_calibs, state_labels = complete_meas_cal(qubit_list=Actual_qbt_lst, qr=qr, circlabel='mcal')

#noise_model = noise.NoiseModel()

#Measure_error = [0.0395, 0.0527, 0.0345, 0.0358, 0.0675, 0.0510, 0.0399, 0.0864, \
#                 0.0992, 0.4447, 0.0551, 0.0436, 0.0454, 0.0531, 0.0795]

#Measure_error = [0.0395, 0.0527, 0.0311, 0.0758, 0.0617,0.0533,0.0342,0.1104,\
#                 0.0604,0.0348,0.0655,0.0527,0.0688, 0.0531]

#for qi in range(7):
#    qbt = Actual_qbt_lst[qi]
#    a = Measure_error[qbt]
#    read_err = noise.errors.readout_error.ReadoutError([[1-a, a],[a,1-a]])
#    noise_model.add_readout_error(read_err, [qi])
# Execute the calibration circuits
#backend_sim = Aer.get_backend('qasm_simulator')
#job = execute(meas_calibs, backend=backend_sim, shots=18192, noise_model=noise_model)

# job = execute(meas_calibs, backend=backend, shots = 8192)#, noise_model=noise_model)

#--------in case we missed---------
#IBMQ.load_account()
#bobychu = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 7 and
#                                                       not x.configuration().simulator)

#backend = least_busy(bobychu)
job=backend.retrieve_job('5de24453bf64f30011c76930')
results = job.result()
#-----------------------------------
cal_results = job.result()
# Calculate the calibration matrix with the noise model
meas_fitter = CompleteMeasFitter(cal_results, state_labels, qubit_list=Actual_qbt_lst, circlabel='mcal')
#print(meas_fitter.cal_matrix)
#-----------------------------


# In[10]:


#from qiskit import IBMQ

#--------------------------------------------------------
#IBMQ.load_account()
#IBMQ.disable_account()
#IBMQ.enable_account('7a7aefd88a5332fcf684d5834e0df990436fcea95871c675109141313ad069356c8cfcd1574cfd88d86766b132123eca2eb9d5733f91c8e02378d118c6d050a7') 
#bobychu = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 7 and
#                                                       not x.configuration().simulator)

#backend = least_busy(bobychu)
#----------------------------------------------------
job_get=backend.retrieve_job('5de2385b111c760012b9ac0c')
results = job_get.result()
#IBMQ.disable_account()

# Results without mitigation
#raw_counts = results.get_counts()
#raw_counts = {'1000110': 1, '0001010': 12, '0000001': 92, '0101001': 1, '0000101': 103, '0100100': 389, '0000011': 7, '0110101': 1, '0100001': 10, '0100110': 18, '0101010': 3, '0110110': 1, '1011000': 1, '0100111': 1, '0100000': 393, '0011101': 1, '0010010': 5, '0111000': 4, '1000100': 19, '0010001': 9, '1000010': 2, '1010000': 1, '0001110': 24, '0100011': 2, '0101110': 3, '0101000': 53, '0011110': 1, '0001111': 2, '1111101': 1, '0000100': 2807, '0101101': 4, '1000001': 1, '0100101': 12, '0010101': 7, '0000000': 2727, '0010100': 110, '0111100': 6, '0010000': 77, '1000000': 23, '0110100': 17, '1001110': 1, '0000110': 116, '0011100': 18, '0011000': 16, '0110010': 2, '0001000': 380, '0001101': 25, '0010110': 8, '0101100': 60, '0000010': 140, '1001000': 4, '0110000': 11, '0001100': 408, '0011001': 1, '1100100': 7, '0000111': 4, '0001001': 11, '1101000': 1, '1001100': 6, '0110001': 1, '1100000': 4, '0100010': 17}

job_get.result().get_counts(0)

# Get the filter object
meas_filter = meas_fitter.filter

# Results with mitigation
mitigated_results = meas_filter.apply(results)
mitigated_counts = mitigated_results.get_counts(0)
print(mitigated_counts)
#print(state_labels)


# In[20]:


print(Actual_qbt_lst)
#print(read_err)
print(P)
#print(mitigated_counts)


# In[4]:


from qiskit.tools.monitor import job_monitor, backend_monitor, backend_overview
backend_monitor(backend)


# In[9]:


job_get=backend.retrieve_job('5d7904f3292eb1001961f023')
dic1 = job_get.result().get_counts()
print(dic1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


# In[4]:


from qiskit.tools.monitor import job_monitor, backend_monitor, backend_overview
backend_monitor(backend)


# In[17]:


from qiskit.quantum_info import state_fidelity

import qiskit.ignis.verification.tomography as tomo
import qiskit.ignis.verification.tomography.fitters.cvx_fit as cvx_fit


# In[20]:


qst = tomo.state_tomography_circuits(circuit, circuit.qubits[10])


# In[21]:


shots = 8192           # Number of shots to run the program (experiment); maximum is 8192 shots.
max_credits = 5        # Maximum number of credits to spend on executions.

job_exp = execute(qst, backend=backend, shots=shots, max_credits=max_credits)
jobID = job_exp.job_id()

print('JOB ID: {}'.format(jobID))


# In[22]:


tomo_fit = tomo.StateTomographyFitter(job_exp.result(), qst)


# In[23]:


rho_cvx = tomo_fit.fit(method='cvx')
rho_mle = tomo_fit.fit(method='lstsq')
print(rho_cvx)


# In[ ]:




