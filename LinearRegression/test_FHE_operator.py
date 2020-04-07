import numpy as np
from customer import customer
from server import server

C = customer(p=65537)
C.save('context', 'pk.key', 'sk.key')

# # test customer encrypt and decrypt
# a = np.array([[1.1, 3.2, 8.1],
#              [1.3, 4.2, 6.3]])
#
# enc_a = C.ecnypt(a)
# print(enc_a)
# print(enc_a.shape)
# dec_a = C.decrypt(enc_a)
# print(dec_a)
# print(dec_a.shape)

###########################
# test operator on server #
###########################
S = server('context', 'pk.key')

# # dot product
# a = np.array([[1, 3, 4]])
# b = np.array([[2, 3.3, 1]])
# b = b.T
# # print(a)
# # print(b)
# # print(a.shape)
# # print(b.shape)
# enc_a = C.ecnypt(a)
# enc_b = C.ecnypt(b)
# enc_a_dot_b = S.dot_product(enc_a, enc_b)
# print(C.decrypt_scalar(enc_a_dot_b))
#
# # matrix multiplication
# a = np.array([[1, 2.2, 3.1],
#               [1.2, 4.1, 3.1]])
#
# b = np.array([[1, 2.2],
#               [1.2, 4.1],
#               [2.1, 2.1]])
#
# enc_a = C.ecnypt(a)
# enc_b = C.ecnypt(b)
# print(enc_a.shape)
# print(enc_b.shape)

# matrix mulmul
a = np.array([[1.73599713],
              [3.02080776],
              [4.3056184 ],
              [5.59042903],
              [6.87523966],
              [8.1600503 ],
              [9.44486093],
              [10.72967157],
              [12.0144822 ],
              [13.29929283],
              [14.58410347],
              [15.8689141 ],
              [17.15372473]])

b = np.array([[ 1.,  1.],
              [ 1.,  2.],
              [ 1.,  3.],
              [ 1.,  4.],
              [ 1.,  5.],
              [ 1.,  6.],
              [ 1.,  7.],
              [ 1.,  8.],
              [ 1.,  9.],
              [ 1., 10.],
              [ 1., 11.],
              [ 1., 12.],
              [ 1., 13.]])

enc_a = C.ecnypt(a)
enc_b = C.ecnypt(b)
print(enc_a.shape)
print(enc_b.shape)
mat_mulmul = S.matrix_mulmul(enc_a, enc_b)
print(C.decrypt(mat_mulmul))

# # matrix subtraction
# a = np.array([[1, 2.2, 3.1],
#               [1.2, 4.1, 3.1]])
# enc_a = C.ecnypt(a)
#
# mat_sub = S.matrix_subtraction(enc_a, enc_a)
# print(C.decrypt(mat_sub))
#
# # matrix addition
# a = np.array([[1, 2.2, 3.1],
#               [1.2, 4.1, 3.1]])
# enc_a = C.ecnypt(a)
#
# mat_add = S.matrix_addition(enc_a, enc_a)
# print(C.decrypt(mat_add))
#
# # matrix square
# a = np.array([[1, 2.2, 3.1],
#               [1.2, 4.1, 3.1]])
# enc_a = C.ecnypt(a)
#
# mat_square = S.matrix_square(enc_a)
# print(C.decrypt(mat_square))
#
# # matrix average
# a = np.array([[1, 2.2, 3.1],
#               [1.2, 4.1, 3.1]])
# enc_a = C.ecnypt(a)
#
# mat_average = S.matrix_average(enc_a, 0)
# print(C.decrypt(mat_average))
#
# mat_average = S.matrix_average(enc_a, 1)
# print(C.decrypt(mat_average))

