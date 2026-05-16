import numpy as np

# ===== Compare with Scalar =====

arr = np.arange(1000)
filter_ = arr % 4 == 0
filtered_arr = arr[filter_]


if __name__ == '__main__':
    print(filtered_arr)


# ===== Elementwise comparison =====

a = np.arange(20).reshape(4, 5)
b = np.arange(0, 25, 6)
compare_a_b = np.equal(a, b)


if __name__ == '__main__':
    print(a)
    print(b)
    print(np.array_equal(compare_a_b, np.array([[True, False, False, False, False],
                                                [False, True, False, False, False],
                                                [False, False, True, False, False],
                                                [False, False, False, True, False]])))

# ===== Find Maxima =====

data = np.genfromtxt('data.csv', delimiter=',', dtype=np.int64)
maxima = np.argmax(data, axis=1)
maxima = np.expand_dims(maxima, axis=1)
result = np.take_along_axis(data, maxima, axis=1)

if __name__ == '__main__':
    print(result)


# ===== Search =====

rng = np.random.default_rng()

temperatures = rng.integers(25, size=7)
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

high = ['High']
low = ['Low']
result = np.where(temperatures > 15, high, low)
warm_days = days[temperatures > 15]

if __name__ == '__main__':
    print(temperatures)
    print(result)
    print(warm_days)


# ===== Find Unique Values =====

csv = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
data, labels = csv[:, 1:], np.array(csv[:, 0], dtype=np.int64)

classes = np.unique(labels)
unique_measurements, unique_data_counts = np.unique(data, return_counts=True)

most_frequent_index = np.argmax(unique_data_counts)
most_frequent_measurement = unique_measurements.flatten()[most_frequent_index]

if __name__ == "__main__":
    print(classes)
    print(unique_data_counts)
    print(most_frequent_index)
    print(most_frequent_measurement)

# ===== Bincount =====

def find_most_frequent_class(data_file):
    csv = np.genfromtxt(data_file, delimiter=',', skip_header=1)
    data, labels = csv[:, 1:], np.array(csv[:, 0], dtype=np.int64)
    counts = np.bincount(labels)

    most_frequent = np.argmax(counts)
    return most_frequent


if __name__ == '__main__':
    most_frequent_class = find_most_frequent_class('data.csv')
    print("Class #", most_frequent_class)

