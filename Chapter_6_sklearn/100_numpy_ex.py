import numpy as np

Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize)) #Z.size =100 Z.itemsize =8

nz = np.nonzero([1,2,0,0,4,0]) #find indices of non-zero elements
print(nz) #(array([0, 1, 4]),)

np.random.random((1,2,3)) #block, columns, rows 

np.diag(np.arange(4)) # values 0,1,2,3 on the diagonal 

Z = np.diag(1+np.arange(4),k=-1) # 5x5 matrix with values 1,2,3,4 just below the diagonal
print(Z) 


