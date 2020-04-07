from Pyfhel import Pyfhel
import numpy as np


class customer():
    def __init__(self, p):
        self.HE = Pyfhel()
        self.HE.contextGen(p=p)
        self.HE.keyGen()

    def save(self, context_path, pk_path, sk_path):
        self.HE.saveContext(context_path)
        self.HE.savepublicKey(pk_path)
        self.HE.savesecretKey(sk_path)

    def ecnypt(self, arr):
        '''
        :param arr: should be float numpy matrix
        :return: encrypted numpy matrix
        '''
        row, col = arr.shape[0], arr.shape[1]
        new_a = []
        for i in range(row):
            row_val = []
            for j in range(col):
                row_val.append(self.HE.encryptFrac(arr[i, j]))
            new_a.append(row_val)
        new_a = np.asarray(new_a)
        return new_a.reshape(row, col)

    def decrypt(self, enc_arr):
        '''
        :param enc_arr: encrypted numpy matrix
        :return: float numpy matrix
        '''
        row, col = enc_arr.shape[0], enc_arr.shape[1]
        new_a = []
        for i in range(row):
            row_val = []
            for j in range(col):
                row_val.append(self.HE.decryptFrac(enc_arr[i, j]))
            new_a.append(row_val)
        new_a = np.asarray(new_a)
        return new_a.reshape(row, col)

    def decrypt_scalar(self, enc_scalar):
        return self.HE.decryptFrac(enc_scalar)
