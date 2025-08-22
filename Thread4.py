import threading
class Box(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)   # super().__init__() # call to parent constructor should be 1st line in child constructor
        self.name=name

    def run(self):
        print(f"Im {self.name} Thread")
        threadLock.acquire() 
        print("Critical section")
        threadLock.release()
        print(f"Exit from {self.name}")



threadLock=threading.Lock()
Thread=[]
t1=Box("Thread-A")
t2=Box("Thread-B")

t1.start()
t2.start()

Thread.append(t1)
Thread.append(t2)

for v in Thread:
    v.join()

print("Exit from Main Thread")
