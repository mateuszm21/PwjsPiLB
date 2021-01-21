from threading import Thread
import random


class Histogram:
    def __init__(self, num_of_bins=10, max_val=100):
        self.max_val = max_val
        self.hist = []
        for _ in range(num_of_bins):
            self.hist.append([])

    def __str__(self):
        step = self.max_val/len(self.hist)
        range_1 = 00
        range_2 = step
        for bin_values in self.hist:
            print(str(int(range_1)) + " - " + str(int(range_2)) + " : " + len(bin_values) * "#")
            range_1 = range_1 + step
            range_2 = range_2 + step
        return "------ Histogram ------"


class HistThread(Thread):
    def __init__(self, thread_id, data, histogram):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.data = data
        self.histogram = histogram

    def fill_hist(self):
        num_of_bins = len(self.histogram.hist)
        max_val = self.histogram.max_val
        step = max_val/num_of_bins

        for i in range(len(self.data)):
            for j in range(num_of_bins):
                if j*step < self.data[i] < (j+1)*step:
                    print("Element assigned to " + str(j) + " bin \n")
                    self.histogram.hist[j].append(data[i])

    def run(self):
        print("Starting thread ID" + str(self.thread_id) + "\n")
        self.fill_hist()
        print("Thread " + str(self.thread_id) + " ended \n")


random.seed()
data = []

for i in range(0, 100):
    data.append(int(random.random() * 100))

hist = Histogram(10, 100)
thread1 = HistThread(1, data[:50], hist)
thread2 = HistThread(2, data[50:], hist)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(hist)
