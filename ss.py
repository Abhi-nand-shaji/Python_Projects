import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You drank coffee")


def drink_coffee():
    time.sleep(4)
    print("You study")


def study():
    time.sleep(5)
    print("You eat breakfast")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

x = threading.Thread(target=drink_coffee, args=())
x.start()

x = threading.Thread(target=study, args=())
x.start()

#eat_breakfast()
#drink_coffee()
#study()


print(threading.active_count())
print(threading.enumerate())

