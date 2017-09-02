"""
This question asks a rewrite of f35q o that is uses n%5 instead of n%3
"""

def f35(n):
    if n < 8:
        return "Error"
    elif n == 8:
        return (1,1)
    elif n == 9:
        return (3,0)
    elif n == 10:
        return (0,2)
    else:
        m3,m5 = f35(n-3)
        return (1+m3,m5)

def f35q(n):
    if n < 8:
        return "Error"
    elif 0 == n%3:
        return (n/3,0)
    elif 1 == n%3:
        return ((n-10)/3,2)
    else:
        return ((n-5)/3,1)

def f35_alt(n):
    if n < 8:
        return "Error"
    elif n == 8:
        return (1, 1)
    elif n == 9:
        return (3, 0)
    elif n == 10:
        return (0, 2)
    elif n == 11:
        return (2, 1)
    elif n == 12:
        return (4, 0)
    else:
        m3, m5 = f35_alt(n-5)
        return (m3, 1+m5)

def f35q_alt(n):
    if n < 8:
        return "Error"
    elif 0 == n%5:
        return (0, n//5)
    elif 1 == n%5:
        return (2, (n-6)//5)
    elif 2 == n%5:
        return (4, (n-12)//5)
    elif 3 == n%5:
        return (1, (n-3)//5)
    else:
        return (3, (n-9)//5)

def validate_tuple(n, tup35):
    m3, m5 = tup35
    return n == (3*m3 + 5*m5)

if __name__ == '__main__':
    test_input = [
        8, 9, 10, 11, 12, 13, 14, 15, 34, 35, 36, 37, 38, 101, 102, 103, 104, 105
    ]
    for t_input in test_input:
        old_val = f35_alt(t_input)
        new_val = f35q_alt(t_input)
        old_valid = validate_tuple(t_input, old_val)
        new_valid = validate_tuple(t_input, new_val)
        print('n =', t_input, '  \t', 'f35 =', old_val, '\t', 'f35q =', new_val, '  \t', 'Valid:', old_valid and new_valid and (old_val == new_val))

