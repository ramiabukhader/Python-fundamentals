import math

x = 1.44
y = -1.44

print(round(x)) # it will give us 1
print(round(y)) # it will give us -1, it will take the nearst integer

print(round(x, 1)) # the nearst decimal

print(math.floor(x)) #it will give the floor value
print(math.ceil(x))
print(math.trunc(x)) # works similar to math.floor, for the positive numbers

print(math.hypot(2, 4)) # pythagoras squareroot( 2**2 + 4**2)

print(math.radians(45)) # 0, 30, 45, 60, 75, 90
print(math.degrees(0.78))
print(math.degrees(math.asin(1))) # pi/2 ==> 90

print(math.acos(1)) # cosine, sin, tan, etc

print('-------')
# pos_inf = float('inf')
# neg_inf = float('-inf')
# not_a_num = float('nan')

pos_inf = math.inf
neg_inf = -math.inf
not_a_num = math.nan