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