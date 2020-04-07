# from Pyfhel import Pyfhel
#
# print("==============================================================")
# print("====================== Pyfhel ENCODING =======================")
# print("==============================================================")
#
#
# print("1. Creating Context and KeyGen in a Pyfhel Object ")
# HE = Pyfhel()                                       # Creating empty Pyfhel object
# HE.contextGen(p=65537)   # Generating context.
# # The values of p and m are chosen to enable batching (see Demo_Batching_SIMD.py)
# HE.keyGen()                                         # Key Generation.
#
# print("2. Encoding integers with encodeInt")
# integer1 = 45
# integer2 = -32
# ptxt_i1 = HE.encodeInt(integer1)   # Encoding integer1 in a new PyPtxt
# ptxt_i2 = HE.encodeInt(integer2)   # Encoding integer2 in a new PyPtxt
#
# print("3. Encrypt plaintext with encryptPtxt")
# ctxt_i1 = HE.encryptPtxt(ptxt_i1)   # Encrypt PyPtxt in a new PyCtxt
# ctxt_i2 = HE.encryptPtxt(ptxt_i2)   # Encrypt PyPtxt in a new PyCtxt
#
# print("4. Operations in the encrypted domain")
# ctx_iadd = ctxt_i1 + ctxt_i2
# ctx_isub = ctxt_i1 - ctxt_i2
# ctx_imul = ctxt_i1 * ctxt_i2
# # ctx_imul = HE.multiply(ctxt_i1, ctxt_i2, True)
#
# print("7. Decrypting result:")
# ptx_iadd = HE.decryptPtxt(ctx_iadd)
# ptx_isub = HE.decryptPtxt(ctx_isub)
# ptx_imul = HE.decryptPtxt(ctx_imul)
#
# print("8. Decoding result:")
# res_iadd = HE.decodeInt(ptx_iadd)
# res_isub = HE.decodeInt(ptx_isub)
# res_imul = HE.decodeInt(ptx_imul)
#
# print("9. Final result:")
# print(res_iadd)
# print(res_isub)
# print(res_imul)

from Pyfhel import Pyfhel

print("==============================================================")
print("====================== Pyfhel ENCODING =======================")
print("==============================================================")


print("1. Creating Context and KeyGen in a Pyfhel Object ")
HE = Pyfhel()                                       # Creating empty Pyfhel object
HE.contextGen(p=65537)   # Generating context.
# The values of p and m are chosen to enable batching (see Demo_Batching_SIMD.py)
HE.keyGen()                                         # Key Generation.

print("2. Encrypt float with encodeFrac")
float1 = 4.5
float1_inv = 1/float1
float2 = -3.2
float2_inv = 1/float2

ctxt_1 = HE.encryptFrac(float1)   # Encrypting float1 in a new PyCtxt
ctxt_2 = HE.encryptFrac(float2)   # Encrypting float2 in a new PyCtxt
ctxt_1_inv = HE.encryptFrac(float1_inv)
ctxt_2_inv = HE.encryptFrac(float2_inv)

print("3. Operations in the encrypted domain")
ctx_add = ctxt_1 + ctxt_2
ctx_sub = ctxt_1 - ctxt_2
ctx_mul = ctxt_1 * ctxt_2
ctx_div = ctxt_1 * ctxt_2_inv

sum = HE.encryptFrac(0)
for i in range(5):
    sum = sum + ctxt_1*ctxt_2
print(HE.decryptFrac(sum))
#
# print("4. Decrypting result:")
# res_add = HE.decryptFrac(ctx_add)
# res_sub = HE.decryptFrac(ctx_sub)
# res_mul = HE.decryptFrac(ctx_mul)
# res_div = HE.decryptFrac(ctx_div)
# res = HE.decryptFrac(a)
# # print("8. Decoding result:")
# # res_iadd = HE.decodeInt(ptx_iadd)
# # res_isub = HE.decodeInt(ptx_isub)
# # res_imul = HE.decodeInt(ptx_imul)
# #
# print("5. Final result:")
# print(res_add)
# print(res_sub)
# print(res_mul)
# print(res_div)
# print(res)