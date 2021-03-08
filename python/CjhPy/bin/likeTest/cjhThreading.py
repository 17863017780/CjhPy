
# 测试多线程使用

from threading import Thread
import time,threading

#打印时间专用
def print_time(threadName):
    print ("%s: %s" % (threadName, time.ctime(time.time())))
        # counter -= 1


# if __name__ == '__main__':
   # for i in range(4):
   #     p = Thread(target=print_time("线程"+str(i)))  # 多进程
   #     p.start()


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 2:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=loop, name='LoopThread1')
t2 = threading.Thread(target=loop, name='LoopThread2')
t3 = threading.Thread(target=loop, name='LoopThread3')
t4 = threading.Thread(target=loop, name='LoopThread4')
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
print('thread %s ended.' % threading.current_thread().name)