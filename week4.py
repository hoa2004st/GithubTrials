### Duplicate check
# n = int(input())
# A = list(map(int, input().split()))
# mem = set()

# for i in range(n):
#     if A[i] in mem:
#         print(1)
#     else:
#         print(0)
#         mem.add(A[i])

### Hash over strings
# def hash(string, m):
#     result = 0
#     for c in string:
#         result = (result * 256 + ord(c)) % m
#     return result

# n, m = map(int, input().split())
# for i in range(n):
#     print(hash(input(), m))

### Sum pair of sequence equal to a number

# n, M = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# i, j = 0, n - 1
# Q = 0
# while i < j:
#     sum = a[i] + a[j]
#     if sum == M:
#         Q += 1
#         i += 1
#         j -= 1
#     elif sum < M:
#         i += 1  
#     else:
#         j -= 1  

# print(Q)


### store & search string
# db = set()
# while True:
#     command = input().split()
#     if command[0] == "*":
#         break
#     elif len(command) == 1:
#         db.add(command[0])
# while True:
#     command = input().split()
#     if command[0] == "***":
#         break
#     if len(command) == 2:
#         x = command[1] in db
#         if command[0] == 'insert':
#             if x:
#                 print(1-int(x))
#             else:
#                 print(1-int(x))
#                 db.add(command[1])
#         elif command[0] == 'find':
#             print(int(x))