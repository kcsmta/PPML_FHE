import numpy as np
import math
from load_data import load_data


def lwlr(X_train, y_train, x, tau=0.01):
    '''
    :param X_train:
    :param y_train:
    :param x: query point
    :param tau: bandwidth parameter
    :return: y - predict value
    '''
    m = X_train.shape[0]
    n = X_train.shape[1]
    y_train=np.reshape(y_train, (m, 1))

    theta = np.zeros((n, 1), dtype='float')
    # print(theta.shape)

    x_tile = np.tile(x.T, [m, 1])
    # print(x_tile)
    # print(x_tile.shape)

    # compute weights
    # w = exp(-sum((X_train - repmat(x', m, 1)).^2, 2) / (2*tau))
    # print(X_train-x_tile)
    norm2 = np.sum(np.abs(X_train-x_tile) ** 2, axis=-1)
    # print(norm2)
    # print(norm2.shape)
    w = np.exp(-norm2/(2*tau**2))
    w = np.reshape(w, (m, 1))
    # print(w)
    # print(w.shape)

    # perform Newton's method
    g = np.ones((n, 1))
    # print(np.sum(np.abs(g)**2)**(1/2))
    n_interation = 1
    max_interation = 1000
    # while (n_interation<max_interation):
    thresh = 1.0
    # while (thresh>10**-6):
    while (n_interation<max_interation):
        # print("interation ", n_interation)
        n_interation+=1
        h = 1. / (1 + np.exp(-X_train.dot(theta)))
        z = w*(y_train - h)
        g = (X_train.T).dot(z) - 0.0001*theta

        tmp = np.reshape(w*h*(1-h), (1, m))
        D = np.diag(tmp[0])
        H = (X_train.T.dot(D)).dot(X_train) - 0.0001*np.eye(n)
        invert_H = np.linalg.inv(H)
        theta = theta - invert_H.dot(g)
        # thresh = np.sum(np.abs(g) ** 2) ** (1 / 2)
        # print(X_train.T)
        # print(z)
        # print(g)
        # print(thresh)
        break

    #return predicted y
    y = float(np.asarray(x).T.dot(theta) > 0)

    return y


# X_train, y_train = load_data()
# i =1
# x = X_train[i]
# x = np.reshape(x, (2, 1))
# # print(x)
# print("y true = ", y_train[i])
# y = lwlr(X_train, y_train, x=x, tau=0.01)
# print("y predict = ", y)
