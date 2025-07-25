import threading
import time

class myThread(threading.Thread):
    def __init__(self , threadId, name , counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
        
    def run(self):
        print("Starting " + self.name)
        #get lock to synchronize threads
        threadLock.acquire()
        print_Time(self.name, self.counter, 3)
        #free lock to released new thread
        threadLock.release()
        
def print_Time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
        
threadLock = threading.Lock()
threads = []

#creating new threads
thread1 = myThread(1, "Threads-1",1)
thread2 = myThread(2, "Threads-2",2)

#Start new threads
thread1.start()
thread2.start()

#Add threads to thread List
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")
        