from threading import Thread, Lock

class Greet:
    # class variables:
    hello_v = 'hello'
    bye_v = 'bye'
    # making the locks & acquiring the bye function
    def __init__(self):
        self.h_lock = Lock()
        self.b_lock = Lock()
        self.b_lock.acquire()

    def hello(self):
        self.h_lock.acquire()
        print(Greet.hello_v, end = '-')
        self.b_lock.release()

    def bye(self):
        self.b_lock.acquire()
        print(Greet.bye_v, end = ' ')
        self.h_lock.release()
# making an object
greet = Greet()

hello = Thread(target = greet.hello, name = 'hello1')
bye = Thread(target = greet.bye, name = 'bye1')
hello2 = Thread(target = greet.hello, name = 'hello1')
bye2 = Thread(target = greet.bye, name = 'bye1')
hello3 = Thread(target = greet.hello, name = 'hello1')
bye3 = Thread(target = greet.bye, name = 'bye1')
# no matters how do these order, the output is 'hello bye hello bye '
bye.start()
hello3.start()
bye2.start()
hello2.start()
hello.start()
bye3.start()