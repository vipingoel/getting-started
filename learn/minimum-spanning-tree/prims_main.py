import sys
from datetime import datetime
import heapq
from dataclasses import dataclass, field
import math

# implementing Prim's algorithm to calculate minimum spanning tree


@dataclass(order=True)
class Vertex:
    i: int = field(compare=False)
    weight: int = field(compare=True)


if __name__ == "__main__":
    print(datetime.now())
    n, m = tuple(map(int, sys.stdin.readline().split()))
    adj_list = [None]*(n+1)
    vertices_in_mst = {}
    for i in range(m):
        a, b, w = tuple(map(int, sys.stdin.readline().split()))
        if not adj_list[a]:
            adj_list[a] = {b: w}
        else:
            adj_list[a][b] = w

        if not adj_list[b]:
            adj_list[b] = {a: w}
        else:
            adj_list[b][a] = w

    start_vertex = Vertex(1, 0)
    vertices = [start_vertex]
    total = 0

    # print("adj_list", adj_list)

    while len(vertices_in_mst) < n:
        v = heapq.heappop(vertices)
        if v.i in vertices_in_mst:
            continue

        vertices_in_mst[v.i] = v.weight
        total += v.weight

        adj_vertices = adj_list[v.i]
        for u, w in adj_vertices.items():
            if u not in vertices_in_mst:
                heapq.heappush(vertices, Vertex(u, w))

        # print("vertices", vertices)
        # print("vertices_in_mst", vertices_in_mst)

    print(total)
    print(datetime.now())
