
# from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        while True:
            print("Hello")
            # sleep(1)
class Hi(Thread):
    def run(self):
        while True:
            print("i")
            # sleep(1)
t1 = Hi()
t2 = Hello()
t1.start()
t2.start()

