# multi thread is like multi tasking
# we achieve it by using Thread super class
# when thread is called main thread divides into multiple paths/threads and executed each threat simultaneoysly
# every task gets time sharing - which is decided by schedular
# we use start , run key words to separatwe actions as threads
# use sleep to allow time to each task to execute simultaneosuly
# use join to end threads and run again as main thread

# by default main thread is executing the code

from threading import *
from time import sleep # used to give sleep/break time to a thread


class Hello(Thread):  # converting class into thread
    def run(self):
        for e in range(10):
            print("helo")
            sleep(1)


class Hi(Thread):
    def run(self):  # run() is a method in Thread superclass - overriding
        for e in range(10):
            print("hi")
            sleep(1)


t1 = Hello()
# to avoid collusion of these two threads usee some sleep
# sleep is - used to give break time for threads

t2 = Hi()

# to create two threads start method is used
# to end Join method is used


t1.start()
sleep(0.3)
t2.start() # starts threads and calls run()print("the end")

# joining threads
t1.join()
t2.join()

print("bye")