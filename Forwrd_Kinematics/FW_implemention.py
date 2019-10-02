
import numpy as np
#due to a problem in calculating trignometric functions I used sympy in calculating 
import sympy as sp
#our function takes 6 joint values as input
def fw(theta1,theta2,theta3,theta4,theta5,theta6):
    rad_value=sp.pi/180
    #the DH paramters for our robot 
    DH_table=[[theta1*rad_value,-90*rad_value,0,360],
              [theta2*rad_value,0*rad_value,420,0],
              [theta3*rad_value,-90*rad_value,0,200],
              [theta4*rad_value,90*rad_value,0,200],
              [theta5*rad_value,-90*rad_value,0,126],
              [theta6*rad_value,0*rad_value,0,20]]
    
    trans=[]
    #loop to calculate every transform starting from T0_1 to T5_6 
    for i in range(6):
        main_matrix=[[sp.cos(DH_table[i][0]),-sp.sin(DH_table[i][0])*sp.cos(DH_table[i][1]),sp.sin(DH_table[i][0])*sp.sin(DH_table[i][1]),DH_table[i][2]*sp.cos(DH_table[i][0])],
                     [sp.sin(DH_table[i][0]),sp.cos(DH_table[i][0])*sp.cos(DH_table[i][1]),-sp.cos(DH_table[i][0])*sp.sin(DH_table[i][1]),DH_table[i][2]*sp.sin(DH_table[i][0])],
                     [0,sp.sin(DH_table[i][1]),sp.cos(DH_table[i][1]),DH_table[i][3]],
                     [0,0,0,1]
                     ]
        #append every trnsform in this list
        trans.append(main_matrix)
    a=np.ones((4,4))
    #loop to multiply all the transforms together in the right order
    #to get the final transform
    for i in range(6):
        a=a.dot(np.array(trans[i]))
    print(a.astype(float))
