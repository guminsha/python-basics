# thread = a flow of execution. Like a separate order of instructions.
#          However, each thread takes a turn running a archive concurrency
#          GIL = (Global interpreter lock),
#          allows one thread to hold the control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensives)
#            better to use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user inputs, web scraping)
#            better to use multithreading

import threading
import time

start = time.perf_counter()


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


# function, args
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# syncs the main thread with the others, having to wait them in this case. x, y and z ends before active_count so only shows 1
x.join()
y.join()
z.join()

# each one at time
# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter() - start)
