#the file contain the fw function
import numpy as np
import FW_implemention
from FW_implemention import trans
#just call the function and put the desired joints angles
v=FW_implemention.fw(90,30,60,90,30,60)
#first joint variables
R_0_0=np.identity(3)
c=np.array([0,0,1])
c=c.reshape(-1,3)
d_0_3=np.array(v[:3,3])
d_0_0=np.zeros((3, 1))
#calculate our R.c
R=R_0_0.dot(c)
#calculate d_0_2 - d_0_0
d=d_0_3-d_0_0

#our first column in jacobian
linear_vel=np.cross(R,d)
rot_vel=R
#stack them togther
jac_mat=np.stack((linear_vel, rot_vel))

#now to get R_0_1 we will use the trans list
R_0_1=np.array(trans[0][:3,:3])
d_0_1=np.array(trans[0][:3,3])
#our second jacobain column
R=R_0_1.dot(c)
d=d_0_3-d_0_1
linear_vel=np.cross(R,d)
rot_vel=R
#stack them
snd_col=np.stack((linear_vel,rot_vel))
jac_mat=np.hstack((jac_mat,2nd_col))

#our third column for the prismatic joint
h_0_2=np.dot(np.array(trans[0]),np.array(trans[1])))
R_0_2=h_0_2[:3,:3]
d_0_2=h_0_2[:3,3]
R=R_0_2.dot(c)
d=d_0_3-d_0_2
linear_vel=np.cross(R,d)
rot_vel=np.zeros(3,1)
#stack them togther
trd_col=np.stack((linear_vel,rot_vel))
jac_mat=np.hstack((jac_mat,3rd_col))

