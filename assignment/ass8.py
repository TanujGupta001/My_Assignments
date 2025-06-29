import numpy as np

empty_array=np.empty((4,3))
print(empty_array)
print()

#--------------------------------------------
import numpy as np
arr=np.full((3,5),0)
print(arr)
print()

#--------------------------------------------
import numpy as np
arr=np.full((4,3,2),1)
print(arr)
print()

#--------------------------------------------
import numpy as np
arr = np.arange(2, 11).reshape(3, 3)
print(arr)
print()

#--------------------------------------------
import numpy as np
arr = np.zeros(10)
arr[5] = 11
print(arr)
print()

#--------------------------------------------
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
reversed_arr = arr[::-1]
print(reversed_arr)
print()

#-------------------------------------------
import numpy as np
arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)
print(float_arr)