import threading
import time

def f1():
    print("f1 thread is started")

    for v in range(6):
        result=v+10
        time.sleep(1)

    else:
        print(f"result: {result}")
    print("Exit from f1 thread")


print("Main Thread:")

obj=threading.Thread(target=f1)   # task for thread

print("Before calling f1 thread")

#   f1() #  direct call to f1()- Single threaded Environment


obj.start()  #   Thread.start()---> Thread.run()--> create a thread & allocate task f1

#   1. MAin Thread     2. obj Thread->task f1

obj.join()   # mainthread will wait for obj thread to complete its execution
for v in range(5):
    time.sleep(1)

print("Main Thread END")





              
