
from sum_ops import sum_ops

if __name__ == '__main__':
    test_inputs = [
        (False, 10, [12, 2, 432, 2, 432, 990, 3, 0, -123, 922, 123]),
        (True, 4, [23, 2, 423423, 2, 42, 90, 7, 102, -3, 942, 10]),
        (True, -1231, [12432, 232, 432432, 23, 432342, 994320, 3423, 2, -1233, 9322, 13423]),
        (False, 9, [9, 23, 4223, 1, 42, 90, 7, 102, -3, 942, 10]),
    ]
    for expected_result, target, els in test_inputs:
        result, lop, rop = sum_ops(els, target)
        print('----')
        print('Input:', target, els)
        print('Result/Expected Result: ', result, expected_result, 'Left and right operand: ', lop, rop)
        print('Outcome:', 'SUCCESS' if result == expected_result else 'FAILURE')
    
