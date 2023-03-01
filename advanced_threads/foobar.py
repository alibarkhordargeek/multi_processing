from threading import Thread, Lock

class FooBar:
    # locking the bar function
    def __init__(self, n):
        self.n = n
        self.foolock = Lock()
        self.barlock = Lock()
        self.barlock.acquire()

    def foo(self, p_foo):
        for _ in range(self.n):
            self.foolock.acquire()
            p_foo()
            self.barlock.release()

    def bar(self, p_bar):
        for _ in range(self.n):
            self.barlock.acquire()
            p_bar()
            self.foolock.release()

def printfoo():
    print('foo', end = '')

def printbar():
    print('bar', end = ' ')
# giving '5' to the object variable
foobar = FooBar(5)

th1 = Thread(target = foobar.foo, args = (printfoo, ))
th2 = Thread(target = foobar.bar, args = (printbar, ))
# prints 'foobar'
th1.start()
th2.start()