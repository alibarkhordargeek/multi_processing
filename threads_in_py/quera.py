import threading
import time

def f1():
    time.sleep(4)
    print(threading.current_thread().name)

def f2():
    time.sleep(3)
    print(threading.current_thread().name)

def f3():
    time.sleep(3.5)
    print(threading.current_thread().name)

def f4():
    time.sleep(2)
    print(threading.current_thread().name)

def g1():
    time.sleep(4)
    print(threading.current_thread().name)

def g2():
    time.sleep(3)
    print(threading.current_thread().name)

def h():
    time.sleep(1.5)
    print(threading.current_thread().name)

th_f1 = threading.Thread(target = f1, name = 'f1')
th_f2 = threading.Thread(target = f2, name = 'f2')
th_f3 = threading.Thread(target = f3, name = 'f3')
th_f4 = threading.Thread(target = f4, name = 'f4')

# starting f funcs
th_f1.start()
th_f2.start()
th_f3.start()
th_f4.start()

# joining f funcs
th_f1.join()
th_f2.join()
th_f3.join()
th_f4.join()

th_g1 = threading.Thread(target = g1, name = 'g1')
th_g2 = threading.Thread(target = g2, name = 'g2')

# after finishing f funcs starts the g funcs
th_g1.start()
th_g2.start()

# joining g funcs
th_g1.join()
th_g2.join()

th_h = threading.Thread(target = h, name = 'h')

# after finishing g funcs starts the h func
th_h.start()