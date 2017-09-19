
from cube_sum import cube_sum

def simpl_sum(n):
    return int((-1)**(n+1)*(.5 * n**3 + .75 * n**2 - 0.125*(1+(-1)**(n+1))))

if __name__ == '__main__':
    for n_pivot in range(1, 100000, 8764):
        for n in range(n_pivot, n_pivot + 4):
            print(n, cube_sum(n), simpl_sum(n))

