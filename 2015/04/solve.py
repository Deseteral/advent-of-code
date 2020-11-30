#!/usr/local/bin/python3
import hashlib
import math
import threading

CORE_COUNT = 6
KEY = "iwrupvqb"

class SearchThread(threading.Thread):
    def __init__(self, count_start, count_end, target):
        threading.Thread.__init__(self)
        self.count_start = count_start
        self.count_end = count_end
        self.target = target

    def run(self):
        search(self.count_start, self.count_end, self.target)

def search(count_start, count_end, target):
    done = False
    num = count_start

    while not done:
        result = hashlib.md5(f"{KEY}{num}".encode()).hexdigest()
        # print(f"{num} {result}")
        if result.startswith(target):
            print(f"result {num}")
            done = True

        if num == count_end:
            done = True

        num += 1

def do_job(count, target, num_threads):
    volume = math.floor(count / num_threads)

    threads = []
    for i in range(num_threads):
        count_start = i * volume
        count_end = (i+1) * volume
        thread = SearchThread(count_start, count_end, target)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

do_job(100_000_000, "000000", CORE_COUNT)
