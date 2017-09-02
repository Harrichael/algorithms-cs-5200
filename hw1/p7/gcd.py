"""
This program creates a new gcd function to return more data than just gcd

Must use recursion
"""

def gcd(a, b):
    rem = a % b
    if 0 == rem:
        return b
    else:
        return gcd(b, rem)

def gcd2(a, b):
    """
    return g,s,t   having the property that g is the GCD of a and b, and s*a + t*b = g
    """
    rem = a % b
    if 0 == rem:
        s = a // b
        t = 1 - s*s
        return b, s, t
    else:
        g, s, t = gcd2(b, rem)
        s = t
        return g, s, (g - a*s)//b

def validate_gcd2(a, b, g, s, t):
    return gcd(a, b) == g and s*a + t*b == g

if __name__ == '__main__':
    test_input = [
        (15, 3),
        (45, 10),
        (135, 20),
        (20, 135),
        (24, 36),
        (35, 20),
        (1010232, 2021878),
        (1581951, 3654084),
    ]

    for t_input in test_input:
        gcd_out = gcd(*t_input)
        gcd2_out = gcd2(*t_input)
        v = validate_gcd2(*t_input, *gcd2_out)
        valid_string = ';a*s + b*t = g;{a}*{s} + {b}*{t} = {g};{sa} + {bt} = {g};{asbt} = {g};{v}'.format(
                a=t_input[0],
                b=t_input[1],
                g=gcd2_out[0],
                s=gcd2_out[1],
                t=gcd2_out[2],
                sa=t_input[0]*gcd2_out[1],
                bt=t_input[1]*gcd2_out[2],
                asbt=t_input[0]*gcd2_out[1] + t_input[1]*gcd2_out[2],
                v=v,
            )
        print('input =', t_input, '\t', 'gcd =', gcd_out, '\t', 'gcd2 =', gcd2_out, '\t')
        valid_string = valid_string.replace(';','\n\t  ')
        print('\tvalid check :', valid_string)

