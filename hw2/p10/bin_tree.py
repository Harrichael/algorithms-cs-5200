
def num_leafs(bin_tree):
    _, left, right = bin_tree
    if left and right:
        return num_leafs(left) + num_leafs(right)
    elif left:
        return num_leafs(left)
    elif right:
        return num_leafs(right)
    else:
        return 1

def num_internals(bin_tree):
    _, left, right = bin_tree
    if not left and not right:
        return 0
    else:
        left_count, right_count = 0, 0
        if left:
            left_count = num_internals(left)
        if right:
            right_count = num_internals(right)
        return 1 + left_count + right_count

def construct_bin_tree(sorted_sequence):
    if not sorted_sequence:
        return []
    seq_len = len(sorted_sequence)
    if seq_len == 1:
        return [sorted_sequence[0], [], []]
    median = sorted_sequence[seq_len//2]
    left = construct_bin_tree(sorted_sequence[0:seq_len//2])
    right = construct_bin_tree(sorted_sequence[seq_len//2+1:seq_len])
    return [median, left, right]

if __name__ == '__main__':
    for depth in range(1, 20):
        num_nodes = 2**depth - 1
        bin_tree = construct_bin_tree(range(num_nodes))
        print('num nodes =', num_nodes, '  \tleafs =', num_leafs(bin_tree), '\tinternals =', num_internals(bin_tree))

