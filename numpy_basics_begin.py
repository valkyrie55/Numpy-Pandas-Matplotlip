import numpy as np
#let create a random data
data = np.random.randn(2,3)
print(data)
#Perform some operations on it
print(data * 10)

print(data + data)
#now create a  2-D numpy array
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)

#Dimensions of the ndarray
print(arr2.ndim)
#----------------------------------------#
#Functions for creating new arrays
print(np.zeros(10)) #ndarray initialized with zero
print(np.zeros((2,3))) # 2X3 ndarray
#-----------------

# To specify data type for an ndarray----------
d = [1,2,3,4,5]
data  = np.array(d,dtype =np.float64)
print(data)
data1 = np.array(d,dtype = np.int32)
print(data1)
#explicitly cast an array from one datatype to another
data3 = data.astype(np.float64)
#Arithmetic operations for np array
data4 =[[1,2,3],[4,5,6]]
data4_ = np.array(data4)
print("-----------------------")
print(data4_)
print(data4_*data4_)
print(data4_ + data4_)