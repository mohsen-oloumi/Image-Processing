import numpy as np 
arr = [[1,2,0],[0,1,1]]
arr = np.asarray(arr)
H = np.dot(arr,arr.T)
eigenval , eigenvec = np.linalg.eig(H)
print "----------A-----------"
print "eigen value is :" ,eigenval
print "eigen vector is :" ,eigenvec
print "----------B-----------"
u, s, vh = np.linalg.svd(arr, full_matrices=True)
print "s is :" ,u 
print "v is :" ,s
print "d is :" ,vh