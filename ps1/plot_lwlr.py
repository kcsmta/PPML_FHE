import numpy as np
from load_data import load_data
from lwlr import lwlr
import matplotlib.pyplot as plt


def plot_lwlr(X, y, tau, res):
    figure = plt.figure()

    x = np.zeros((2, 1))
    pred = np.zeros((res, res), dtype=float)

    for i in range(0, res):
        for j in range(0, res):
            x[0] = 2 * i / (res - 2) - 1
            x[1] = 2 * j / (res - 2) - 1
            pred[j, i] = lwlr(X, y, x, tau)
            if pred[j, i] == 0:
                plt.plot(x[0], x[1], 'bo')
            else:
                plt.plot(x[0], x[1], 'ro')
            # print(x, pred[j, i])

    for i, x in enumerate(X):
        if y[i] == 0:
            plt.plot(x[0], x[1], 'ko')
        else:
            plt.plot(x[0], x[1], 'kx')

    plt.show()


    # imagesc(pred, [-0.4 1.3]);
    # plot((res / 2) * (1 + X(y == 0, 1)) + 0.5, (res / 2) * (1 + X(y == 0, 2)) + 0.5, 'ko');
    # plot((res / 2) * (1 + X(y == 1, 1)) + 0.5, (res / 2) * (1 + X(y == 1, 2)) + 0.5, 'kx');

X_train, y_train = load_data()
plot_lwlr(X_train, y_train, tau=0.01, res=50)
