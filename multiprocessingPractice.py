##import time
##import multiprocessing 
##def dosomething():
##    print("Sleeping for one sec")
##    time.sleep(1)
##    print("Done Sleeping")
##
##p1 = multiprocessing.Process(target=dosomething)
##p2 = multiprocessing.Process(target=dosomething)
##
##p1.start()
##p2.start()
##
##finish = time.perf_counter()
##print("Finished in ", finish, "second(s)")
import threading
import random
list1 = []
list2 = []
def gatherData():
    global list1
    global list2
    for i in range(10):
        rand = random.randint(1,100)
        list1.append(rand)
    print(list1)

def pushData():
    global list1
    global list2
    for i in list1:
        list2.append(i)
    print(list2)

t1 = threading.Thread(target =gatherData)
t2 = threading.Thread(target=pushData)

t1.start()
t2.start()
t1.join()
t2.join()
print("Thread Completed")
