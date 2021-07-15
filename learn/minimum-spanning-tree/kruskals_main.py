import sys
from datetime import datetime
# implementing kruskal's algorithm to find the minimum spanning tree


class DisjointSets:
    def __init__(self, n):
        self.arr = list(range(n+1))
        self.sizes = [1]*(n+1)

    def root(self, i):
        parent = self.arr[i]
        while parent != i:
            # this statement is using the path compression
            self.arr[i] = self.arr[parent]
            i = parent
            parent = self.arr[parent]
        return i

    def join(self, a, b):
        # joining b to a
        # using root based method with balancing
        root_a = self.root(a)
        root_b = self.root(b)
        if self.sizes[root_a] > self.sizes[root_b]:
            self.arr[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.arr[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]

    def connected(self, a, b):
        return self.root(a) == self.root(b)


if __name__ == "__main__":
    print(datetime.now())
    n, m = tuple(map(int, sys.stdin.readline().split()))
    edges = [None]*m
    for i in range(m):
        edges[i] = list(map(int, sys.stdin.readline().split()))

    # sort by weight
    edges.sort(key=lambda edge: edge[2])
    print(datetime.now())

    vertices = DisjointSets(n)
    total_weight = 0
    edge_count = 0
    for edge in edges:
        a, b, w = tuple(edge)
        if not vertices.connected(a, b):
            vertices.join(a, b)
            total_weight += w
            edge_count += 1
            if edge_count == n-1:
                break
    print(total_weight)
    print(datetime.now())
