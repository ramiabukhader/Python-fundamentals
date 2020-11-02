import hashlib
import random

h = hashlib.new('sha256')
h.update(b'I know Arabic')
print(h.digest())
print('---')

print(h.hexdigest())


# hashing a file
hasher = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
print(hasher)
# SIZE = 65536
# with open('myfile', 'r',) as f:
#     burffer = f.read(SIZE)
#     while len(burffer) > 0:
#         hasher.update(burffer)
#         burffer = f.read(SIZE)

# print(hasher.hexdigest())