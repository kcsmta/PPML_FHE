import numpy as np
from Pyfhel import Pyfhel


class server():
    def __init__(self, context_path, pk_path):
        self.HE = Pyfhel()
        self.HE.restoreContext(context_path)
        self.HE.restorepublicKey(pk_path)

    def encrypt(self, arr):
        '''
        :param arr: should be float numpy matrix
        :return: encrypted numpy matrix
        '''
        row, col = arr.shape[0], arr.shape[1]
        new_a = []
        for i in range(row):
            row_val = []
            for j in range(col):
                row_val.append(self.HE.encryptFrac(arr[i][j]))
            new_a.append(row_val)
        new_a = np.asarray(new_a)
        return new_a.reshape(row, col)

    def dot_product(self, ctxt1, ctxt2):
        '''
        :param ctxt1: encrypted numpy array, size (1xm)
        :param ctxt2: encrypted numpy 1D array, size (mx1)
        :return:
        '''
        assert ctxt1.shape[1] == ctxt2.shape[0], "error size of array in dot product"
        sum = self.HE.encryptFrac(0)
        for i in range(ctxt1.shape[1]):
            sum = sum + ctxt1[0][i]*ctxt2[i][0]
        return sum

    def matrix_multiplication(self, ctx1, ctx2):
        '''
        :param ctx1: encrypted matrix, size (mxn)
        :param ctx2: encrypted matrix, size (nxp)
        :return: encrypted matrix, size (mxp)
        '''
        assert ctx1.shape[1] == ctx2.shape[0], "error size of array in matrix multiplication"
        row, col = ctx1.shape[0], ctx2.shape[1]
        temp = np.zeros((row, col))
        res = self.encrypt(temp)

        for i in range(row):
            for j in range(col):
                sum = self.HE.encryptFrac(0)
                for k in range(ctx1.shape[1]):
                    sum = sum + ctx1[i][k] * ctx2[k][j]
                res[i][j] = sum
        return res

    def matrix_mulmul(self, ctx1, ctx2):
        '''
        :param ctx1: encrypted matrix, size (mx1)
        :param ctx2: encrypted matrix, size (mxp)
        :return: encrypted matrix, size (mxp)
        '''
        assert ctx1.shape[0] == ctx2.shape[0], "error size of array in matrix mulmul"
        row, col = ctx2.shape[0], ctx2.shape[1]
        temp = np.zeros((row, col))
        res = self.encrypt(temp)

        for i in range(row):
            for j in range(col):
                res[i][j] = ctx1[i][0]*ctx2[i][j]
        return res

    def matrix_scalar_mul(self, ctx1, enc_scalar):
        '''
        :param ctx1: encrypted matrix, size (mxn)
        :return: encrypted matrix, size (mxn)
        '''
        row, col = ctx1.shape[0], ctx1.shape[1]
        temp = np.zeros((row, col))
        res = self.encrypt(temp)

        for i in range(row):
            for j in range(col):
                res[i][j] = enc_scalar*ctx1[i][j]
        return res

    def matrix_subtraction(self, ctx1, ctx2):
        '''
        :param ctx1: encrypted matrix, size (mxn)
        :param ctx2: encrypted matrix, size (mxn)
        :return: encrypted matrix, size (mxn)
        '''
        assert ctx1.shape[0] == ctx2.shape[0] and ctx1.shape[1]==ctx2.shape[1], "error size of array in matrix subtraction"
        row, col = ctx1.shape[0], ctx1.shape[1]
        temp = np.zeros((row, col))
        res = self.encrypt(temp)

        for i in range(row):
            for j in range(col):
                res[i][j] = ctx1[i][j] - ctx2[i][j]
        return res

    def matrix_addition(self, ctx1, ctx2):
        '''
        :param ctx1: encrypted matrix, size (mxn)
        :param ctx2: encrypted matrix, size (mxn)
        :return: encrypted matrix, size (mxn)
        '''
        assert ctx1.shape[0] == ctx2.shape[0] and ctx1.shape[1]==ctx2.shape[1], "error size of array in matrix subtraction"
        row, col = ctx1.shape[0], ctx1.shape[1]
        temp = np.zeros((row, col))
        res = self.encrypt(temp)

        for i in range(row):
            for j in range(col):
                res[i][j] = ctx1[i][j] + ctx2[i][j]
        return res

    def matrix_square(self, ctx1):
        '''
        :param ctx1: encrypted matrix, size (mxn)
        :return: encrypted matrix, size (mxn)
        '''
        row, col = ctx1.shape[0], ctx1.shape[1]
        temp = np.zeros((row, col))
        res = self.encrypt(temp)

        for i in range(row):
            for j in range(col):
                res[i][j] = ctx1[i][j] * ctx1[i][j]
        return res

    def matrix_average(self, ctx1, axis=0):
        assert axis == 0 or axis == 1, "axis can be only 0 or 1"
        row, col = ctx1.shape[0], ctx1.shape[1]

        if axis == 0:
            temp = np.zeros((1, col))
            res = self.encrypt(temp)
            enc_row_inv = self.HE.encryptFrac(1.0/row)
            for i in range(col):
                sum = self.HE.encryptFrac(0)
                for j in range(row):
                    sum = sum + ctx1[j][i]
                res[0][i]=sum*enc_row_inv
            return res

        if axis == 1:
            temp = np.zeros((row, 1))
            res = self.encrypt(temp)
            enc_col_inv = self.HE.encryptFrac(1.0/col)
            for i in range(row):
                sum = self.HE.encryptFrac(0)
                for j in range(col):
                    sum = sum + ctx1[i][j]
                res[i][0]=sum*enc_col_inv
            return res
