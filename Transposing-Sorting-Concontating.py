import numpy as np

# ===== Transpose =====

a = np.array([['clear', 'usually', 'of'],
              ['conscience', 'the', 'bad'],
              ['is', 'sign', 'memory']])
a = a.transpose(1, 0)

b = np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]])
b = b.transpose(0, 1)
np.reshape()
c = np.array([np.arange(0, 12, 2).reshape(3, 2).transpose(), np.arange(1, 13, 2).reshape(3, 2).transpose()])


if __name__ == '__main__':
    print(a)
    print(b)
    print(c)


# ===== Transpose 1D =====

def reshape_transpose(start, stop, step=1):
    # Create a 1D array using arange function
    # Reshape the 1D array so that you can transpose it
    a = np.arange(start, stop, step)
    a = a.reshape(1, a.size)
    return a.T


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))


# ===== Sorting =====

rng = np.random.default_rng()

a = rng.integers(100, size=(5, 20))


b = np.sort(a, axis=0)
ind = np.argsort(b, axis=1)
c = np.take_along_axis(b, ind, axis=1)


if __name__ == '__main__':
    print('\nUnsorted array:\n', a)
    print('\nSorted columns:\n', b)
    print('\nIndices to sort rows:\n', ind)
    print('\nSorted:\n', c)


# ===== Indirect partial sort =====

rng = np.random.default_rng()

k = 3
mu = 1
sigma = 1
arr = rng.normal(mu, sigma, 20)
target = 0
distances = abs(arr - target)

indices = np.argpartition(distances, k)
partitioned_by_distance = arr[indices]
k_nearest = partitioned_by_distance[:k]

if __name__ == '__main__':
    print('Data:\n', arr)
    print('\nDistances from target value:\n', distances)
    print('\nIndices of partitioned data:\n', indices)
    print('\nPartitioned data:\n', partitioned_by_distance)
    print('\nK=3 nearest data points\n', k_nearest)


# ===== Concatenate and Stack ===== 

a = np.zeros((3, 4), dtype=np.int64)
b = np.arange(4).reshape(1, 4)
c = np.concatenate((a, b), axis=0)

stacked = np.vstack((np.arange(10), np.arange(20, 30), np.arange(40, 50)))

if __name__ == '__main__':
    print(c)
    print(stacked)


# ===== Split =====

x = np.arange(24).reshape(6, 4)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]
# [16 17 18 19]
# [20 21 22 23]]

arr1, arr2, arr3 = np.split(x, 3)

y = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

arr4, arr5, arr6 = np.array_split(y, 3, axis=1)

if __name__ == '__main__':
    print(arr1, '\n', arr2, '\n', arr3, '\n')
    print(arr4, '\n', arr5, '\n',  arr6)