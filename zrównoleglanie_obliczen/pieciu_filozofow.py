from threading import Thread, Lock
import time
import random


class Philosopher(Thread):
    running = True

    def __init__(self, index, left_fork, right_fork):
        Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            time.sleep(1)
            print("Philosopher " + str(self.index) + " is hungry" + "\n")
            self.consume()

    def consume(self):
        fork1, fork2 = self.left_fork, self.right_fork
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print("Philosopher " + str(self.index) + " swaps forks" + "\n")
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()

        fork2.release()
        fork1.release()

    def dining(self):
        print("Philosopher " + str(self.index) + " starts eating" + "\n")
        time.sleep(1)
        print("Philosopher " + str(self.index) + " finishes eating" + "\n")


forks = []
philosophers = []

for i in range(0, 5):
    forks.append(Lock())

for i in range(0, 5):
    philosophers.append(Philosopher(str(i), forks[i % 5], forks[(i + 1) % 5]))

Philosopher.running = True
random.seed()

for i in range(0, 5):
    philosophers[i].start()

time.sleep(30)
Philosopher.running = False
print("The end")
