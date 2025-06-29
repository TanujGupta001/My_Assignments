import numpy as np
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6],[7, 8, 9]])
a_reshaped = a.reshape(1, 3)
combined = np.concatenate((a_reshaped, b), axis=0)
print(combined)
print()


#------------------------------------
import numpy as np
arr = np.array([[1, 2], [3, 4]])
flattened = arr.flatten()
print(flattened)
print()


#------------------------------------
import numpy as np
arr=np.array([1,2,3,4])
print(arr)
reversed_arr=arr[::-1]
print(reversed_arr)
print()


#------------------------------------
import numpy as np
arr = np.array([[10, 20], [30, 40]])
print(arr.max())
print(arr.min())
rows, cols = arr.shape
print(rows)
print(cols)
print(arr[0])
print(arr[1][0])
total = 0
for row in arr:
    for val in row:
        total += val
print(total)
brr = np.array([[1, 2], [3, 4]])
print(arr + brr)
print(arr - brr)
print(arr * brr)
print(arr / brr)