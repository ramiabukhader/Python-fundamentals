from random import randint

print(randint(0, 5)) # it will take a random number between those values
print('----------')
#advanced password generator using python
from string import punctuation, ascii_letters, digits
import random
symbols = punctuation + ascii_letters + digits # collection of characters

secured_random = random.SystemRandom()
password = "-".join(secured_random.choice(symbols) for i in range(10))
print(password)

#shuffle

collectio = ['ram', 'cd', 'harddisk']
random.shuffle(collectio)
print(collectio)

print(random.choice(collectio))

# print(random.randrange(100))
#or 
print(random.randrange(10, 20, 3)) #10 to 19 ==>[10, 13, 16, 19]

#seed created a fixed random number series
random.seed(5)
print(random.randrange(0, 10))
print(random.randrange(0,10))