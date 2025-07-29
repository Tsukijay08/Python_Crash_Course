import threading
import time

def foo():
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        print("working on a task")
        time.sleep(1)
    print("Stopping the Thread after some time")
    
#Creating a thread
t = threading.Thread(target = foo)
t.start()

#allow the thread to run in 5 seconds
time.sleep(5)

#set the termination flag to stop the thread
t.do_run = False