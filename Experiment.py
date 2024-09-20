from threading import Thread
def one():
    while True:
        print(1)
def two():
    while True:
        print(2)
t1 = Thread(target=one)
t2 = Thread(target=two)
t1.start()
t2.start()
t2.join()
thread_running = False