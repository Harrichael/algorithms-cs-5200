
import random
import time

from sum_ops import sum_ops

class Timer(object):
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = None

    def __exit__(self, *args, **kwargs):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time

def random_test_case(set_len):
    els = []
    for _ in range(set_len):
        els.append(random.randint(-10000,10000))

    target = random.randint(-20000, 20000)
    return target, els

if __name__ == '__main__':
    test_time_sums = {}
    timer = Timer()

    trials_per_len = 20
    test_cases = list(range(10, 3000))
    for set_len in test_cases:
        test_time_sums[set_len] = 0
        for _ in range(trials_per_len):
            target, els = random_test_case(set_len)
            with timer:
                sum_ops(els, target)
                
            test_time_sums[set_len] += timer.elapsed_time

    for set_len in test_cases:
        print(set_len, ',', test_time_sums[set_len]/trials_per_len)

