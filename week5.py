###Hamiton Cycle
# def check_hamilton(n, m, edges):
#     def backtrack(current, visited):
#         if len(visited) == n and 1 in edges[current]:
#             return True
#         for node in edges[current]:
#             if node not in visited:
#                 visited.add(node)
#                 if backtrack(node, visited):
#                     return True
#                 visited.remove(node)
#         return False

#     visited = set([1])
#     if backtrack(1, visited):
#         return 1
#     return 0

# T = int(input())
# for i in range(T):
#     n, m = map(int, input().split())
#     edges = {i + 1: [] for i in range(n)}
#     for j in range(m):
#         x, y = map(int, input().split())
#         edges[x].append(y)
#         edges[y].append(x)
#     print(check_hamilton(n, m, edges))


###List order of nodes visited by a DFS
# def DFS(current, edges, visited):
#     if len(visited) == len(edges):
#         return visited
#     for node in edges[current]:
#         if node not in visited:
#             visited.append(node)
#             DFS(node, edges, visited)
#     return visited

# n, m = map(int, input().split())
# edges = {i + 1: [] for i in range(n)}
# for j in range(m):
#     x, y = map(int, input().split())
#     edges[x].append(y)
#     edges[y].append(x)
# for node in edges:
#     edges[node].sort()

# result = DFS(1, edges, [1])
# print(*result)

###List order of nodes visited by a BFS
# def BFS(start, edges, visited):
#     visited.append(start)
#     queue = [start]

#     while queue:
#         current = queue.pop(0)
#         for node in edges[current]:
#             if node not in visited:
#                 visited.append(node)
#                 queue.append(node)
#     return visited

# n, m = map(int, input().split())
# edges = {i + 1: [] for i in range(n)}
# for j in range(m):
#     x, y = map(int, input().split())
#     edges[x].append(y)
#     edges[y].append(x)
# for node in edges:
#     edges[node].sort()

# visited = []
# for i in range(1, n+1):
#     if i not in visited:
#         BFS(i, edges, visited)
# print(*visited)

###Minimum Spanning Tree - Kruskal

# class Tree:
#     def __init__(self, n):
#         self.parent = list(range(n))

#     def root(self, u):m
#         if self.parent[u] != u:
#             self.parent[u] = self.root(self.parent[u])
#         return self.parent[u]

#     def union(self, u, v):
#         root_u = self.root(u)
#         root_v = self.root(v)

#         if root_u != root_v:
#             self.parent[root_v] = root_u
#             return True
#         return False

# def kruskal(n, edges):
#     edges.sort(key=lambda x: x[2])
#     ds = Tree(n)
#     weight = 0
#     n_edges = 0

#     for u, v, w in edges:
#         if ds.union(u - 1, v - 1):
#             weight += w
#             n_edges += 1
#             if n_edges == n - 1:
#                 break

#     return weight


# n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#     u, v, w = map(int, input().split())
#     edges.append((u, v, w))
# result = kruskal(n, edges)
# print(result)