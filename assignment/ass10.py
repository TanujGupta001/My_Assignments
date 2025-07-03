#question 1
import numpy as np
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr, nan=0)
arr = arr.T
print("Modified Array:\n", arr)

#question 2
import numpy as np
arr = np.random.randint(0, 10, (2, 3, 4))
print("Original shape:", arr.shape)
new = np.moveaxis(arr, 1, -1)
print("New shape after moveaxis:", new.shape)

#question 3
import numpy as np
arr = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]], dtype=float)
col = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col, inds[1])
print("Array after replacing NaNs with column averages:\n", arr)

#question 4
import numpy as np
arr = np.array([[1, -2, 3], [-4, 5, -6]])
arr[arr < 0] = 0
print("Array after replacing negatives with 0:\n", arr)

#question 6
import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
print("Array 1:", arr1)
print("Array 2:", arr2)

#question 7
from scipy import stats
import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:\n", avg)

arr_2d_1 = np.random.randint(0, 100, (3, 3))
arr_2d_2 = np.random.randint(0, 100, (3, 3))
combined = np.concatenate((arr_2d_1.flatten(), arr_2d_2.flatten()))
mean = np.mean(combined)
median = np.median(combined)
mode = stats.mode(combined, keepdims=True)[0]
print("Mean:", mean, "Median:", median, "Mode:", mode)

#question 8
import numpy as np
A = np.array([[1, -2, 3], [-1, 3, -2], [2, -5, 5]])
b = np.array([9, -6, 17])
x = np.linalg.solve(A, b)
print("Solution using linalg.solve:\n", x)


A_inv = np.linalg.inv(A)
x_inv = A_inv.dot(b)
print("Solution using inverse matrix method:\n", x_inv)

#question 9
import matplotlib.pyplot as plt
sem1 = [75, 80, 85, 90, 95]
sem2 = [78, 82, 88, 92, 96]
students = ['S1', 'S2', 'S3', 'S4', 'S5']

plt.plot(students, sem1, label='Semester 1', linestyle='--', marker='o')
plt.plot(students, sem2, label='Semester 2', linestyle='-', marker='x')
plt.title('Semester Comparison')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.legend()
plt.grid(True)
plt.show()