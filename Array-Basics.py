import numpy as np

# ===== N-Dimensional Arrays (ndarray) =====

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(type(arr), arr[2][0]) # indexing (row, column)
print(f'Number of dimensions: {arr.ndim}\n')
print(f'Number of Rows and Columns respectively: {arr.shape}\n')
print(f'Size of the array (shape[0] * shape[1]): {arr.size}\n')
print(f'Data type of the array: {arr.dtype}\n\n')


# ===== Creation of an array =====

# By default, the dtype of an array is float64
# but it can be specified dtype

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Whole array is created

a = np.zeros((3, 3)) # Creates an array full of zeros
b = np.ones((3, 3), dtype=np.int16) # Creates an array full of zeros
c = np.full((3, 3), True) # Creates an array full of specifed values

print(f'{a}\n\n{b}\n\n{c}\n\n')


# ===== Create and Array from Range =====

# np.arange(start, end, step)
a1 = np.arange(0, 10, 2)
b1 = np.arange(0, 10, 0.2)
c1 = np.arange(10)

# np.arange(start, end, number of elements)
d1 = np.linspace(0, 10, 5)

print(f'{a1}\n\n{b1}\n\n{c1}\n\n{d1}\n\n')


# ===== Reading and Writing files =====

# Reads the file and turns it into array
# textArr = np.loadtxt('file.txt', delimiter=',', skiprows=1);

# Also puts NaN in missing values
# textArr = np.genfromtxt('file.csv', delimiter=',', skip_header=1);

# Saves the text in the new file
# np.savetxt('test.out', textArr, delimiter=',')


# ===== Random Sampling & Shuuffling =====

# Returns random floats in the interval [0.0, 1.0]
x = np.random.random(5);

# Create a random generator
rng = np.random.default_rng()

# Returns random integers in the interval [0, end] using generator
y = rng.integers(1000)
v = rng.integers(10, size=15)
f = rng.integers(100, size=(2, 4), endpoint=True);

print(f'{x}\n\n{y}\n\n{v}\n\n{f}\n\n')

# Function random.Generator.permutation randomly permutes
# a sequence or returns a permuted range.

arr1 = np.arange(9).reshape((3, 3))
print(rng.permutation(arr1, axis=1), '\n\n')


# Function random.Generator.shuffle modifies an array
# or sequence in-place by shuffling its contents.


arr2 = np.arange(9).reshape((3, 3))
rng.shuffle(arr2, axis=1)


print(f'{arr2}\n\n')