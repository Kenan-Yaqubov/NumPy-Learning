import numpy as np

# ===== Indexing Basics =====

x = np.arange(40).reshape(10, 4)

# Array x:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  [24 25 26 27]
#  [28 29 30 31]
#  [32 33 34 35]
#  [36 37 38 39]]

a = x[4, 3]
b = x[::2, ::2].reshape(5, 2)


if __name__ == '__main__':
    print(a)
    print(b)


# ===== Integer Array Indexing =====

x = np.arange(35)
y = x.reshape(5, 7)

a = x[np.array([7, 13, 28, 33])]
b = x[np.array([[0, 1, 2], [10, 11, 12], [28, 29, 30]])]


c = y[np.array([0, 2, 4])]
d = y[np.array([0, 2, 4]), np.array([0, 1, 2])]
e = y[np.array([1, 2, 4]), 6]


if __name__ == '__main__':
    print(y)
    print('\n', a.shape)
    print('\n', b.shape)
    print('\n', c.shape)
    print('\n', d.shape)
    print('\n', e.shape)


# ===== Boolean Indexing =====

a = np.arange(20).reshape(2, 2, 5)
mask = np.array([[True, False], [False, True]])
c = a[mask]

if __name__ == '__main__':
    print('Array a:\n', a, '\n')
    print('Indexed array c:\n', c)
    print(c.shape)
