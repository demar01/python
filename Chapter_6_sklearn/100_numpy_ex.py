import numpy as np

Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize)) #Z.size =100 Z.itemsize =8

nz = np.nonzero([1,2,0,0,4,0]) #find indices of non-zero elements
print(nz) #(array([0, 1, 4]),)

np.random.random((1,2,3)) #block, columns, rows 

np.diag(np.arange(4)) # values 0,1,2,3 on the diagonal 

Z = np.diag(1+np.arange(4),k=-1) # 5x5 matrix with values 1,2,3,4 just below the diagonal
print(Z) 


Z = np.ones((5,3)) @ np.ones((3,2)) #matrix multiplication
print(Z)

Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1 #change sing in this range
print(Z)

Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2)) # find common values

np.datetime64('today') + np.timedelta64(1)# numpy can also be used for dates that can be used in arrays


A = np.ones(3)*1
B = np.ones(3)*2
np.add(A,B,out=B) #will store it in B, without making a copy.

#5x5 matrix with row values ranging from 0 to 4

Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)

# without broadcasting
Z = np.tile(np.arange(0, 5), (5,1))
print(Z)

#sum a small array faster than np.sum
Z = np.arange(10)
np.add.reduce(Z)