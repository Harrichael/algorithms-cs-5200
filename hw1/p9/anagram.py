"""
This file creates two anagram generators and compares them
"""

import time
import string

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

def anagram1(string):
    """
    This anagram func uses multiple recursive calls
    """
    if string == '':
        return ['']
    else:
        anagrams = []
        for i, c in enumerate(string):
            string_part = string[:i] + string[i+1:]
            for sub_anagram in anagram1(string_part):
                new_anagram = c + sub_anagram
                anagrams.append(new_anagram)

        return anagrams

def anagram2(string):
    """
    This anagram func uses one recursive call
    """

    if not string:
        return ['']
    else:
        anagrams = []
        head = string[0]
        tail = string[1:]
        for sub_anagram in anagram2(tail):
            for i in range(len(sub_anagram)+1):
                new_anagram = sub_anagram[:i] + head + sub_anagram[i:]
                anagrams.append(new_anagram)

        return anagrams            

if __name__ == '__main__':
    test_funcs = [anagram1, anagram2]
    test_cases = list(range(11))
    min_repeats = 3
    max_repeats = 100
    min_time = 5
    timer = Timer()
    data = {}
    for func in test_funcs:
        data[func.__name__] = dict([(n, []) for n in test_cases])

    for string_len in test_cases:
        test_string = string.ascii_uppercase[:string_len]
        for func in test_funcs:
            test_repeats = 0
            test_case_time = 0
        
            while (test_repeats < max_repeats) and (test_repeats < min_repeats or test_case_time < min_time):
                with timer:
                    func(test_string)

                data[func.__name__][string_len].append(timer.elapsed_time)

                test_repeats += 1
                test_case_time += timer.elapsed_time

    print('func,' + ','.join(map(str, test_cases)))
    for func in test_funcs:
        f_data = data[func.__name__]
        best_times = [min(f_data[tc]) for tc in test_cases]
        print(func.__name__ + ',' + ','.join(map(str, best_times)))

