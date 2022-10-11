import numpy as np
n1 = int(input("Enter the order of the matrix"))
array1 = np.random.randint(10, size=(n1,n1))
array2 = np.random.randint(10, size=(n1,n1))
print("this is array1")
print(array1)
print("this is array2")
print(array2)

add = np.add(array1,array2)
print("the result matrix is")
print(add)
