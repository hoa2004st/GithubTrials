#####All pair shortest paths (directed, positive)

# def FW(n, edges):
#     result = [[float('inf')] * n for _ in range (n)]

#     for i in range(n):
#         result[i][i] = 0
    
#     for u, v, w in edges:
#         result[u-1][v-1] = min(result[u-1][v-1], w)
    
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if result[i][k] < float('inf') and result[k][j] < float('inf'):
#                     result[i][j] = min(result[i][j], result[i][k] + result[k][j])
    
#     for i in range(n):
#         for j in range(n):
#             if result[i][j] == float('inf'):
#                 result[i][j] = -1

#     return result


# n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#     u, v, w = map(int, input().split())
#     edges.append((u, v, w))

# result = FW(n, edges)
# for row in result:
#     print(*row)

##### Max Flow
# from collections import deque
# def BFS(capacity, s, t, prev):
#     n = len(capacity)
#     visited = [False] * n
#     queue = deque([s])
#     visited[s] = True

#     while queue:
#         u = queue.popleft()
#         for v in range(n):
#             if not visited[v] and capacity[u][v] > 0:
#                 queue.append(v)
#                 visited[v] = True
#                 prev[v] = u
#                 if v == t:
#                     return True
#     return False

# def MF(n, capacity, s, t):
#     prev = [-1] * n
#     max_flow = 0

#     while BFS(capacity, s, t, prev):
#         flow = float('inf')
#         u = t
#         while u != s:
#             flow = min(flow, capacity[prev[u]][u])
#             u = prev[u]

#         v = t
#         while v != s:
#             u = prev[v]
#             capacity[u][v] -= flow
#             capacity[v][u] += flow
#             v = u

#         max_flow += flow

#     return max_flow

# n, m = map(int, input().split())
# s, t = map(int, input().split())
# s -= 1
# t -= 1

# capacity = [[0] * n for _ in range(n)]

# for _ in range(m):
#     u, v, c = map(int, input().split())
#     u -= 1
#     v -= 1
#     capacity[u][v] += c

# result = MF(n, capacity, s, t)
# print(result)

##### Shortest Path
# import heapq
# import sys
# input = sys.stdin.read
# output = sys.stdout.write

# def dijkstra(n, edges, s, t):
#     graph = [[] for _ in range(n)]
#     for u, v, w in edges:
#         graph[u-1].append((v-1, w))

#     dist = [float('inf')] * n
#     dist[s-1] = 0
#     pq = [(0, s-1)]

#     while pq:
#         d, u = heapq.heappop(pq)
        
#         if u == t-1:
#             return d
        
#         if d > dist[u]:
#             continue

#         for v, w in graph[u]:
#             if dist[u] + w < dist[v]:
#                 dist[v] = dist[u] + w
#                 heapq.heappush(pq, (dist[v], v))
    
#     return -1 if dist[t-1] == float('inf') else dist[t-1]

# # Faster input/output
# def main():
#     data = input().split()
#     idx = 0
#     n, m = int(data[idx]), int(data[idx + 1])
#     idx += 2
#     edges = []
#     for i in range(m):
#         u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
#         edges.append((u, v, w))
#         idx += 3
#     s, t = int(data[idx]), int(data[idx + 1])

#     result = dijkstra(n, edges, s, t)
#     output(f"{result}\n")

# if __name__ == "__main__":
#     main()