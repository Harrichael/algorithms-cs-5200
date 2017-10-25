
import argparse
import random
from time import time

from tree import Tree

def test_insertion_contains(tree, value):
    is_new_value = value not in tree

    tree.insert(value)

    if value not in tree:
        return False

    if is_new_value:
        tree.remove(value)
        return value not in tree

    return True

def test_deletion_contains(tree, value):
    tree.remove(value)

    if value in tree:
        return False

    tree.insert(value)

    return value in tree

def main(num_tests, base_size, gen_value):
    test_funcs = [
            test_insertion_contains,
            test_deletion_contains,
        ]

    tree = Tree()
    for value in [gen_value() for _ in range(base_size)]:
        tree.insert(value)

    for _ in range(num_tests):
        test_func = test_funcs[random.randint(0, len(test_funcs)-1)]
        value = gen_value()
        if not test_func(tree, value):
            print('FAILURE: {} on value {}'.format(test_func.__name__, value))
            break
    else:
        print('SUCCESS')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Binary Tree Quick Tester')
    parser.add_argument('--num_tests', type=int, default=100, help='Number of tests to perform on tree')
    parser.add_argument('--base_size', type=int, default=1000, help='Base tree size')
    parser.add_argument('--min_value', type=int, default=0, help='Min value to generate for testing')
    parser.add_argument('--max_value', type=int, default=10000, help='Max value to generate for testing')
    parser.add_argument('--seed', type=int, default=None, help='Seed to use for testing')
    
    args = parser.parse_args()
    gen_value = lambda: random.randint(args.min_value, args.max_value)
    if args.seed is None:
        args.seed = int(time() * 1000)

    random.seed(args.seed)

    print('Test Seed: {}'.format(args.seed))
    main(args.num_tests, args.base_size, gen_value)



    

