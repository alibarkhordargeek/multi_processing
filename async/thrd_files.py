from threading import Thread
import time

def txt_file1():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\1.txt', 'x')
    num = 1000000
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')
    print(f"txt file 1 finished at {time.strftime('%X')}")

def txt_file2():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 2
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')
    print(f"txt file 1 finished at {time.strftime('%X')}")

def txt_file3():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 3
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

def txt_file4():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 4
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

def txt_file5():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 5
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

def txt_file6():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 6
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')
def txt_file7():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 7
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

def txt_file8():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 8
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

def txt_file9():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 9
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

def txt_file10():
    print(f"txt file 1 started at {time.strftime('%X')}")
    f = open('D:\\2.txt', 'x')
    num = 1000000 * 10
    for i in range(1, num):
        f.write(f'{i}\n')
    f.write(f'{num}')

file1 = Thread(target = txt_file1)
file2 = Thread(target = txt_file2)
file3 = Thread(target = txt_file3)
file4 = Thread(target = txt_file4)
file5 = Thread(target = txt_file5)
file6 = Thread(target = txt_file6)
file7 = Thread(target = txt_file7)
file8 = Thread(target = txt_file8)
file9 = Thread(target = txt_file9)
file10 = Thread(target = txt_file10)

file1.start()
file2.start()
file3.start()
file4.start()
file5.start()
file6.start()
file7.start()
file8.start()
file9.start()
file10.start()