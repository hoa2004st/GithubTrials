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