import math
import heapq as h
import os.path

def prim(G, start):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [math.inf]*n

    cost[start] = 0
    q = [(0, start)]
    while q:
        _, u = h.heappop(q)
        if visited[u]: continue
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < cost[v]:
                cost[v] = w
                path[v] = u
                h.heappush(q, (w, v))

    return path

p = None
if os.path.exists("result.path"):
    f = open('result.path')
    data = f.readlines()[0]
    p = [int(x) for x in data.split()]
