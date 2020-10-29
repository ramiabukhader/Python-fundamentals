#downloading several pages of a website and compile them into a single page
# from queue import Queue

# # example of Queue

# question_queue = Queue()

# for x in range(1, 10):
#     temp_dic = ('key', x)
#     question_queue.put(temp_dic)
# while (not question_queue.empty()):
#     item = question_queue.get()
#     print(str(item))

import requests
from threading import Thread
from queue import Queue

q = Queue(maxsize = 20)

def put_page_to_q(page_num):
    q.put(requests.get('http://google.com/pages_%s.html' %page_num))

def compile(q):
    if not q.full():
        raise ValueError
    else:
        print('Done Compiling')

threads = []
for page_num in range(20):
    t = Thread(target=put_page_to_q, args= (page_num,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

compile(q)
print(threads)