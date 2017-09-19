
from tabulate import tabulate

def rec_sum(n):
    if n <= 1:
        return 1
    else:
        sign = (-1)**(n-1)
        return sign * n**3 + rec_sum(n-1)

if __name__ == '__main__':
    last_abs_num = None
    output = []
    output.append(['n', 'S(n)', 'A(n)=|S(n)|', 'B(n)=A(n)-A(n-1)', 'C(n)=B(n)-B(n-1)', 'C(n)-C(n-1)'])
    diff_array = [[None]*3]
    for index, el in enumerate(range(1, 21)):
        num = rec_sum(el)
        abs_num = abs(num)

        last_diff = last_abs_num
        diff = abs_num
        new_diffs = []
        for new_diff in diff_array[index]:
            curr_diff = diff - last_diff if last_diff else None
            new_diffs.append(curr_diff)
            last_diff = new_diff
            diff = curr_diff

        diff_array.append(new_diffs)
        output.append([el, num, abs_num, *new_diffs])

        last_abs_num = abs_num

    print(tabulate(output))

