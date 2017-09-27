

def complement(target, op):
    return target - op

def bounded_sum_ops(els, target):
    left_index = 0
    right_index = len(els) - 1
    while left_index != right_index:
        left_value = els[left_index]
        right_value = els[right_index]

        if left_value + right_value == target:
            return True, left_value, right_value

        if complement(target, right_value) > right_value:
            break

        if complement(target, left_value) < left_value:
            break

        if complement(target, left_value) < right_value:
            right_index -= 1
        else:
            left_index += 1

    return False, None, None

def sum_ops(els, target):
    return bounded_sum_ops(list(sorted(els)), target)

