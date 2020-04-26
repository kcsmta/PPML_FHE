import numpy as np


def load_data():
    X = np.loadtxt('./data/x.dat', dtype='float')
    y = np.loadtxt('./data/y.dat')
    return X, y

# X, y = load_data()
# print(X)
# print(type(X))
# print(X.shape)
#
# print(y)
# print(type(y))
# print(y.shape)