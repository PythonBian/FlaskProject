"""
当前文档的目的是为了回忆协程
"""
'''
#生成器
def hello():
    for i in (1,10,3):
        key = yield i
        print(key)
        print("hello world")

h = hello()
print("++++++++++++++++++++++++++++++++++++++++")
print(next(h))
print("++++++++++++++++++++++++++++++++++++++++")
print(next(h))
print("++++++++++++++++++++++++++++++++++++++++")

#send方法
print("++++++++++++++++++++++++++++++++++++++++")
print(next(h))
print("++++++++++++++++++++++++++++++++++++++++")
print(h.send(10))
print("++++++++++++++++++++++++++++++++++++++++")
print(h.send(20))
print("++++++++++++++++++++++++++++++++++++++++")

#在实际工作当中，协程至少需要两个函数
def getContent():
    """
    获取内容的方法
    """
    while True:
        url = yield "I have content"
        print("get content from url:%s"%url)


def getUrl(g):
    url_list = ["url1","url2","url3","url4","url5"]
    for i in url_list:
         print("+++++++++++++++++++++++++++++++++++++")
         g.send(i)
         print("+++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    g = getContent()
    print(next(g))
    getUrl(g)

#https://blog.csdn.net/u014331598/article/details/84622652
'''
# gevent

# import gevent
#
# def fun1():
#     for i in range(5):
#         print("I am fun 1 this is %s"%i)
#         gevent.sleep(0)
#
# def fun2():
#     for i in range(5):
#         print("I am fun 2 this is %s"%i)
#         gevent.sleep(0)
#
# # fun1()
# # fun2()
#
# t1 = gevent.spawn(fun1)
# t2 = gevent.spawn(fun2)
#
# gevent.joinall([t1,t2])

import gevent
from gevent.lock import Semaphore

sem = Semaphore(1)

def fun1():
    for i in range(5):
        sem.acquire()
        print("I am fun 1 this is %s"%i)
        sem.release()
def fun2():
    for i in range(5):
        sem.acquire()
        print("I am fun 2 this is %s"%i)
        sem.release()

# fun1()
# fun2()

t1 = gevent.spawn(fun1)
t2 = gevent.spawn(fun2)

gevent.joinall([t1,t2])




