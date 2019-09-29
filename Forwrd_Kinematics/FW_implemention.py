
import numpy as np
#due to a problem in calculating trig func. i used sympy
import sympy as sp
def fw(theta1,theta2,theta3,theta4,theta5,theta6):
    rad_value=sp.pi/180
    DH_table=[[theta1*rad_value,-90*rad_value,0,360],
              [theta2*rad_value,0*rad_value,420,0],
              [theta3*rad_value,-90*rad_value,0,200],
              [theta4*rad_value,90*rad_value,0,200],
              [theta5*rad_value,-90*rad_value,0,126],
              [theta6*rad_value,0*rad_value,0,20]]
    trans=[]
    for i in range(6):
        main_matrix=[[sp.cos(DH_table[i][0]),-sp.sin(DH_table[i][0])*sp.cos(DH_table[i][1]),sp.sin(DH_table[i][0])*sp.sin(DH_table[i][1]),DH_table[i][2]*sp.cos(DH_table[i][0])],
                     [sp.sin(DH_table[i][0]),sp.cos(DH_table[i][0])*sp.cos(DH_table[i][1]),-sp.cos(DH_table[i][0])*sp.sin(DH_table[i][1]),DH_table[i][2]*sp.sin(DH_table[i][0])],
                     [0,sp.sin(DH_table[i][1]),sp.cos(DH_table[i][1]),DH_table[i][3]],
                     [0,0,0,1]
                     ]
        trans.append(main_matrix)
    a=np.ones((4,4))
    for i in range(6):
        a=a.dot(np.array(trans[i]))
    print(a.astype(float))