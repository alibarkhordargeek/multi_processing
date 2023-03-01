from threading import Thread, Lock

class Foo:
    # locking the 'second' & 'third' functions
    def __init__(self):
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, print_func):
        print_func()
        self.lock2.release()

    def second(self, print_func):
        self.lock2.acquire()
        print_func()
        self.lock3.release()

    def third(self, print_func):
        self.lock3.acquire()
        print_func()

def print1():
    print('1', end = ' ')

def print2():
    print('2', end = ' ')

def print3():
    print('3', end = ' ')
# making the object
foo = Foo()

th1 = Thread(target = foo.first, args = (print1, ))
th2 = Thread(target = foo.second, args = (print2, ))
th3 = Thread(target = foo.third, args = (print3, ))
# with any kind of order, it will finall print: '1 2 3'
th3.start()
th2.start()
th1.start()