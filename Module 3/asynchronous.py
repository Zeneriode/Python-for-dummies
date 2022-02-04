import threading


X = 0


def a(b, event_for_wait, event_for_set):
    global X
    for i in range(10):
        event_for_wait.wait()
        event_for_wait.clear()
        print(b)
        print(X)
        X += 1
        event_for_set.set()


def c(d, event_for_wait, event_for_set):
    global X
    for i in range(10):
        event_for_wait.wait()
        event_for_wait.clear()
        print(d)
        print(X)
        X += 1
        event_for_set.set()


event1 = threading.Event()
event2 = threading.Event()

thread1 = threading.Thread(target=a, args=(1, event1, event2))
thread2 = threading.Thread(target=c, args=(2, event2, event1))

thread1.start()
thread2.start()

event1.set()
