#the file contain the fw function
import numpy as np
import FW_implemention
from FW_implemention import trans
#just call the function and put the desired joints angles
v=FW_implemention.fw(90,30,60,90,30,60)
#first joint variables
Rotaion_part=v[:3,:3]
postion_part=v[:3,3]

r,p,y = symbols('r p y')
# Roll
ROT_x = Matrix([[       1,       0,       0],
                [       0,  cos(r), -sin(r)],
                [       0,  sin(r),  cos(r)]])
# Pitch
ROT_y = Matrix([[  cos(p),       0,  sin(p)],
                [       0,       1,       0],
                [ -sin(p),       0,  cos(p)]])
# Yaw
ROT_z = Matrix([[  cos(y), -sin(y),       0],
                [  sin(y),  cos(y),       0],
                [       0,       0,       1]])

ROT_EE = ROT_z * ROT_y * ROT_x
ROT_corr = ROT_z.subs(y, radians(180)) * ROT_y.subs(p, radians(-90))
ROT_EE = ROT_EE * ROT_corr
ROT_EE = ROT_EE.subs({'r': roll, 'p': pitch, 'y': yaw})

WC = EE - (0.303) * ROT_EE[:,2]
theta1 = atan2(WC[1],WC[0])
A = 1.501
C = 1.25
B = sqrt(pow((sqrt(WC[0]*WC[0] + WC[1]*WC[1]) - 0.35), 2) + pow((WC[2] - 0.75), 2))
a = acos((B*B + C*C - A*A) / (2*B*C))
b = acos((A*A + C*C - B*B) / (2*A*C))
c = acos((A*A + B*B - C*C) / (2*A*B))
theta2 = pi/2 - a - atan2(WC[2]-0.75, sqrt(WC[0]*WC[0]+WC[1]*WC[1])-0.35)
theta3 = pi/2 - (b+0.036) # 0.036 accounts for sag in link4 of -0.054m
R0_3 = T0_1[0:3,0:3] * T1_2[0:3,0:3] * T2_3[0:3,0:3]
R0_3 = R0_3.evalf(subs={q1: theta1, q2: theta2, q3:theta3})
R3_6 = R0_3.inv(method="LU") * ROT_EE
theta5 = atan2(sqrt(R3_6[0,2]*R3_6[0,2] + R3_6[2,2]*R3_6[2,2]),R3_6[1,2])
if (theta5 > pi) :
    theta4 = atan2(-R3_6[2,2], R3_6[0,2])
    theta6 = atan2(R3_6[1,1],-R3_6[1,0])
else:
    theta4 = atan2(R3_6[2,2], -R3_6[0,2])
    theta6 = atan2(-R3_6[1,1],R3_6[1,0])
FK = T0_7.evalf(subs={q1:theta1,q2:theta2,q3:theta3,q4:theta4,q5:theta5,q6:theta6})
