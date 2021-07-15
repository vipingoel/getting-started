#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


def bfs(n, m, edges, s):
    # Write your code here
    nodes = [None]*(n+1)
    # lets make the graph
    for edge in edges:
        a, b = tuple(edge)
        if not nodes[a]:
            nodes[a] = [b]
        else:
            nodes[a].append(b)

        if not nodes[b]:
            nodes[b] = [a]
        else:
            nodes[b].append(a)

    # now lets traverse:
    visited = [False]*(n+1)
    queue = deque([s])
    visited[s] = True

    distances = [-1]*(n+1)
    distances[s] = 0

    while len(queue) > 0:
        node = queue.popleft()
        distance_to_childs = distances[node]+6
        childs = nodes[node]
        if not childs:
            continue

        for child in childs:
            if not visited[child]:
                visited[child] = True
                distances[child] = distance_to_childs
                queue.append(child)

    return distances[1:s] + distances[s+1:]


if __name__ == '__main__':

    q = int(sys.stdin.readline().strip())

    for q_itr in range(q):
        first_multiple_input = sys.stdin.readline().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, sys.stdin.readline().rstrip().split())))

        s = int(sys.stdin.readline().strip())

        result = bfs(n, m, edges, s)

        print(' '.join(map(str, result)))
        # print('\n')

    # fptr.close()
