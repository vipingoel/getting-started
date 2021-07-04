#!/bin/python3

import math
import os
import random
import re
import sys

# Hacker Rank - Disjoint sets
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


class Sets:
    def __init__(self, n):
        self.arr = list(range(n))
        # self.counts = {i:1 for i in self.arr}
        self.roots = {i: 0 for i in self.arr}

    def root_of(self, i):
        while self.arr[i] != i:
            i = self.arr[i]
        return i

    def count_elements_in_roots(self):
        print("arr", self.arr)
        print("roots", self.roots)
        for element in self.arr:
            root = self.root_of(element)
            self.roots[root] += 1

    def join(self, x, y):
        count = 0
        x_offset = x-1
        y_offset = y-1

        root_x = self.root_of(x_offset)
        root_y = self.root_of(y_offset)
        if root_x == root_y:
            # same root, so already joined
            return

        self.arr[root_x] = root_y
        if root_x in self.roots:
            # if root_x == 72:
            #     print("join - deleting 72:", x_offset, y_offset, root_x, root_y)
            del self.roots[root_x]

        # temp = self.arr[x_offset]
        # for i in range(len(self.arr)):
        #     # print("arr", self.arr)
        #     # print("counts", self.counts)
        #     if self.arr[i] == temp:
        #         self.arr[i] = self.arr[y_offset]
        #         if i in self.counts:
        #             del self.counts[i]
        #         # count += 1
        #     elif self.arr[i] == self.arr[y_offset]:
        #         # count += 1

        # self.counts[y_offset] = count
        # print("arr", self.arr)
        # print("counts", self.counts)


def componentsInGraph(gb):
    # Write your code here
    sets = Sets(2*len(gb))
    for conn in gb:
        count = sets.join(*tuple(conn))

    max_set = 1
    min_set = 2*len(gb)
    sets.count_elements_in_roots()
    # for root in sets.roots:

    for val in sets.roots.values():
        if val > 1:
            max_set = max(max_set, val)
            min_set = min(min_set, val)
    return [min_set, max_set]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
