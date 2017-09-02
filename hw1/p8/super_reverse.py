"""
This file creates a recursive list reverser
"""

def super_reverse(els):
    rev_els = []
    for el in reversed(els):
        if isinstance(el, list):
            rev_els.append( super_reverse(el) )
        else:
            rev_els.append(el)
    
    return rev_els

if __name__ == '__main__':
    test_input = [
        [2, 3, [11, 23, 1, 45, 2, [232, 23], 3], 4, [2, 5], 2],
    ]

    for t_input in test_input:
        out = super_reverse(t_input)
        print('input =\t\t', t_input)
        print('super_reverse =\t', out)

