import numpy as np
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
from matplotlib.pyplot import ion, show
np.random.seed(0)


def hypothesis(theta, X):
    tempX = np.ones((X.shape[0], X.shape[1] + 1))
    tempX[:, 1:] = X
    return np.matmul(tempX, theta)


def loss(theta, X, y):
    return np.average(np.square(y - hypothesis(theta, X))) / 2


def gradient(theta, X, Y) :
    tempX = np.ones((X.shape[0], X.shape[1] + 1))
    tempX[:,1:] = X
    # print((Y - hypothesis(theta, X)))
    # print(tempX)
    # print((Y - hypothesis(theta, X)) * tempX)
    # print(np.average((Y - hypothesis(theta, X)) * tempX, axis= 0))
    print((Y - hypothesis(theta, X))*tempX)
    d_theta = - np.average((Y - hypothesis(theta, X)) * tempX, axis= 0)
    # print((Y - hypothesis(theta, X)).shape)
    # print(tempX.shape)
    # print(((Y - hypothesis(theta, X)) * tempX).shape)
    # d_theta = - np.sum((Y - hypothesis(theta, X)) * tempX, axis=0)
    d_theta = d_theta.reshape((d_theta.shape[0], 1))
    return d_theta


def gradient_descent(theta, X, Y, learning_rate, max_iteration, gap):
    cost = np.zeros(max_iteration)
    for i in range(max_iteration) :
        d_theta = gradient(theta, X, Y)
        theta = theta - learning_rate * d_theta
        cost[i] = loss(theta, X, Y)
        if i % gap == 0:
            print('epoch : ', i+1, ' loss : ', loss(theta, X, Y))
            ion()
            plt.plot(X.T, y.T, 'ro')  # data
            plt.plot(X, hypothesis(theta, X))  # the fitting line
            plt.xlabel('X')
            plt.ylabel('y')
            if i < max_iteration-1:
                show()
                plt.pause(0.001)
                plt.clf()
            else:
                show()
                plt.pause(3)

    return theta, cost


# # height (cm)
# X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# # weight (kg)
# y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# y = 2x + 1
X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]).T
y = np.array([[3, 5, 7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27]]).T


# X = normalize(X, axis=0)
# y = normalize(y, axis=0)
# print(X)
# print(y)

# print(X)
# print(X.shape)
# print(y)
# print(y.shape)

theta = np.random.rand(X.shape[1]+1, 1)

# print(theta)
# print(theta.shape)
learning_rate = 0.01
max_iteration = 2
theta, cost = gradient_descent (theta, X, y, learning_rate, max_iteration, 1)
print(theta)
