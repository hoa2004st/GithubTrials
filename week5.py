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