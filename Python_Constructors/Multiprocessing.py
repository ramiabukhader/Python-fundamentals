import multiprocessing as mp

#countUp()
#countDown()

import time
from random import randint

def countUp():
    i = 0
    while i <= 3:
        print("Up: \t {}".format(i))
        time.sleep(randint(1, 3))
        i += 1

def countDown():
    i = 3
    while i >= 0:
        print("Down: \t {}".format(i))
        time.sleep(randint(1, 3))
        i -= 1

if __name__ == "__main__":
    #initiate the worker
    workerUp = mp.Process(target=countUp())
    workerDown = mp.Process(target=countDown())

    # Start the workers
    workerUp.start()
    workerDown.start()

    # make worker to join
    workerUp.join()
    workerDown.join()

from multiprocessing import Pool
def cube(x):
    return x**3

if __name__ == "__main__":
    pool = Pool(5)
    result = pool.map(cube, [1, 2, 3, 4, 5, 6 , 66, 7,7333, 4345])
    print(result)