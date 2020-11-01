import hashlib # for password hashing

import os

# Salt: additional random number of characters, it is added to the password to make it more complicated.

salt = os.urandom(16) #sixteen bits

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed) # the available algorithms for hasing

hash = hashlib.pbkdf2_hmac('sha256', b'rami001@', salt, 100000)

print(hash)

import binascii
hexhash = binascii.hexlify(hash)
print(hexhash) # we printed the encrypted value of the password