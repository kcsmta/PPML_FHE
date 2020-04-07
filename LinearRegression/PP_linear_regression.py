import numpy as np
from customer import customer
from server import server
np.random.seed(0)

C = customer(p=65537)
C.save('context', 'pk.key', 'sk.key')


###########################
#      customer side      #
###########################
X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]).T
y = np.array([[3, 5, 7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27]]).T
enc_X = C.ecnypt(X)
enc_y = C.ecnypt(y)

###########################
#       server side       #
###########################
S = server('context', 'pk.key')


def hypothesis_fhe(enc_theta, enc_X):
    '''
    :param enc_theta: theta in form ciphertext
    :param enc_X: X in form ciphertext
    :return: scalar value in ciphertext
    '''
    tempX = np.ones((X.shape[0], X.shape[1] + 1))
    tempX[:, 1:] = enc_X
    enc_tempX = S.encrypt(tempX)
    return S.matrix_multiplication(enc_tempX, enc_theta)


def loss_fhe(enc_theta, enc_X, enc_y):
    n = S.HE.encryptFrac(1.0 / 2)
    return S.matrix_average(S.matrix_square(S.matrix_subtraction(enc_y, hypothesis_fhe(enc_theta, enc_X))), axis=0)[0][0] * n


def gradient_fhe(enc_theta, enc_X, enc_y) :
    tempX = np.ones((enc_X.shape[0], enc_X.shape[1] + 1))
    tempX[:,1:] = enc_X
    enc_tempX = S.encrypt(tempX)

    enc_tmp1 = S.matrix_subtraction(enc_y, (hypothesis_fhe(enc_theta, enc_X)))
    enc_tmp2 = enc_tempX
    enc_res1 = S.matrix_mulmul(enc_tmp1, enc_tmp2)
    print(C.decrypt(enc_tmp1))
    print(C.decrypt(enc_tmp2))
    print(C.decrypt(enc_res1))

    z = S.HE.encryptFrac(-1.0)
    enc_tmp = S.matrix_average(S.matrix_mulmul(S.matrix_subtraction(enc_y, (hypothesis_fhe(enc_theta, enc_X))), enc_tempX), axis=0).T
    d_theta = S.matrix_scalar_mul(enc_tmp, z)
    # d_theta = - np.sum((Y - hypothesis(theta, X)) * tempX, axis=0)
    d_theta = d_theta.reshape((d_theta.shape[0], 1))
    return d_theta


def gradient_descent(enc_theta, enc_X, enc_y, enc_learning_rate, max_iteration, gap):
    for i in range(max_iteration) :
        d_theta = gradient_fhe(enc_theta, enc_X, enc_y)
        enc_theta = enc_theta - S.matrix_scalar_mul(d_theta, enc_learning_rate)
        if i % gap == 0:
            print('epoch : ', i+1, ' loss : ', loss_fhe(enc_theta, enc_X, enc_y))
            # print('epoch : ', i + 1, ' loss : ', C.decrypt_scalar(loss_fhe(enc_theta, enc_X, enc_y)))

    return enc_theta


theta = np.random.rand(X.shape[1]+1, 1)
enc_theta = S.encrypt(theta)
# print(theta)
# print(theta.shape)
learning_rate = 0.01
enc_learning_rate = S.HE.encryptFrac(learning_rate)
max_iteration = 2
enc_theta = gradient_descent(enc_theta, enc_X, enc_y, enc_learning_rate, max_iteration, 1)


###########################
#      customer side      #
###########################
print(C.decrypt(enc_theta))
