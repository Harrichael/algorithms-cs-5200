"""
This file answers problem 3: 

Write a simple Python function that produces the alternating
difference of a list of numbers. For example:
altDif([3 5 4]) = 3 - (5 - 4) = 3 - 1 = 2
altDif([6 7]) = 6-7 = -1
"""

def alt_diff(nums):
    if not nums:
        return 0
    else:
        head, *tail = nums
        diff_val = head - alt_diff(tail)
        return diff_val

if __name__ == '__main__':
    print(alt_diff([3, 5, 4]))
    print(alt_diff([6, 7]))

