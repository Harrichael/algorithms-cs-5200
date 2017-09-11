
def num_leafs(bin_tree):
    _, left, right = bin_tree
    if not left and not right:
        return 1
    else:
        left_count, right_count = 0, 0
        if left:
            left_count = num_leafs(left)
        if right:
            right_count = num_leafs(right)
        return left_count + right_count

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
    for bin_tree_len in range(1, 101):
        bin_tree = construct_bin_tree(range(bin_tree_len))
        print('size(tree) =', bin_tree_len, ' \tleafs =', num_leafs(bin_tree), '\tinternals =', num_internals(bin_tree))

