import threading
class Box(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)   # super().__init__() # call to parent constructor should be 1st line in child constructor
        self.name=name

    def run(self):
        print(f"Im {self.name} Thread")

print("Main Thread Started")
obj=Box("Thread1")
obj.start() #obj.run()
print("Exit from Main Thread")










    
