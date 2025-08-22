import time
import threading
def f1():
    print("Im f1 task-Thread")
    for v in range(5):
        time.sleep(1)
    print("Exit from f1 task-Thread")

def f2():
    print("Im f2 task-Thread")
    for v in range(5):
        time.sleep(1)
    print("Exit from f2 task-Thread")

print("\t Main Thread ")

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
print("\t   After calling f1 task- Thread")


t2.start()
print("\t   After calling f2 task- Thread")

#1. Main Thread   2. t1 Thread    3. t2 Thread
t1.join() # main thread waits until t1 completes f1 task
t2.join()  # main Thread waits until t2 completes f2 task
print("\n Exit from Main thread")
