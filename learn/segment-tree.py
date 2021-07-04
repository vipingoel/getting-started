'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
sys.setrecursionlimit(200000)


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        possible_segment_nodes = (2*len(self.arr)-1)
        self.seg = [0]*possible_segment_nodes
        self.build(0, 0, len(arr)-1)

    def __repr__(self):
        return repr(self.seg)

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def parent(self, i):
        return (i-1)//2

    # builds a segment tree with min value of each segment
    def build(self, i, l, r):
        if l == r:
            self.seg[i] = self.arr[l]
            return

        mid = (l+r)//2
        left = self.left(i)
        right = self.right(i)
        self.build(left, l, mid)
        self.build(right, mid+1, r)
        self.seg[i] = min(self.seg[left], self.seg[right])

    def update(self, x, y):
        self._update(0, 0, len(self.arr)-1, x, y)

    def _update(self, i, l, r, x, y):
        if l == r:
            self.arr[x] = y
            self.seg[i] = y
            return

        mid = (l+r)//2
        left = self.left(i)
        right = self.right(i)
        if l <= x and x <= r:
            self._update(left, l, mid, x, y)
        else:
            self._update(right, mid+1, r, x, y)

        self.seg[i] = min(self.seg[left], self.seg[right])

    def minimum(self, l, r):
        return self._minimum(0, 0, len(self.arr)-1, l, r)

    def _minimum(self, i, start, end, l, r):
        if l > end or r < start:
            # range is outside the given node range
            return 1000000
        elif l <= start and r >= end:
            return self.seg[i]
        else:
            mid = (start+end)//2
            left_min = self._minimum(self.left(i), start, mid, l, r)
            right_min = self._minimum(self.right(i), mid+1, end, l, r)
            # print("left_min", left_min)
            # print("right_min", right_min)
            return min(left_min, right_min)


def main():
    n, queries = tuple(list(map(int, input().split())))
    arr = list(map(int, input().split()))
    segment_tree = SegmentTree(arr)
    # print(segment_tree)
    for i in range(queries):
        query = input().split()
        if query[0] == "u":
            segment_tree.update(int(query[1])-1, int(query[2]))
        elif query[0] == "q":
            print(segment_tree.minimum(int(query[1]) - 1, int(query[2]) - 1))
        else:
            raise Exception("invalid query type")


main()
