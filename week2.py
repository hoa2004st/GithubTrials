### nCk
# def combination(k, n, tbl):
#     if (k, n) in tbl:
#         return tbl[(k, n)]
#     elif k == 0 or k == n:
#         return 1
#     else:
#         result = combination(k-1, n-1, tbl) + combination(k, n-1, tbl)
#         tbl[(k, n)] = result
#         return result
    
# tbl = {}
# k, n = [int(x) for x in input().split()]

# if n > 200:
#     for i in range(n//200):
#         combination(i*100, i*200, tbl)

# print(combination(k, n, tbl) % (10**9 + 7))

###permutation generation
# n = int(input())
# prev_perm = [[1, 2], [2, 1]]
# for i in range(3, n+1):
#     perms = []
#     for perm in prev_perm:
#         for j in range(i-1, -1, -1):
#             temp = perm[:]
#             temp.insert(j, i)
#             perms.append(temp)
#     prev_perm = perms

# result = [" ".join([str(x) for x in perm]) for perm in perms]
# result.sort()
# print('\n'.join(result))

###fibonacci
# n = int(input())
# mem = {}
# def fib(x, mem):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     elif x in mem:
#         return mem[x]
#     else:
#         result = fib(x-1, mem) + fib(x-2, mem)
#         mem[x] = result
#         return result
    
# print(fib(n-1, mem))

###Sudoku solution count
# def check(sudoku_tbl, i, j, value):
#     for k in range(9):
#         if sudoku_tbl[i][k] == value or sudoku_tbl[k][j] == value:
#             return False
#     for m in range(3):
#         for n in range(3):
#             if sudoku_tbl[i//3*3 + m][j//3*3 + n] == value:
#                 return False
#     return True

# def back_track(sudoku_tbl, i, j):
#     if sudoku_tbl[i][j] != 0:
#         if i == 8 and j == 8:
#             count[0] += 1
#         elif j == 8:
#             back_track(sudoku_tbl, i+1, 0)
#         else:
#             back_track(sudoku_tbl, i, j+1)
#     else:
#         for value in range(1, 10):
#             if check(sudoku_tbl, i, j, value):
#                 sudoku_tbl[i][j] = value
#                 if i == 8 and j == 8:
#                     count[0] += 1
#                 elif j == 8:
#                     back_track(sudoku_tbl, i+1, 0)
#                 else:
#                     back_track(sudoku_tbl, i, j+1)
#                 sudoku_tbl[i][j] = 0

# sudoku_tbl = []
# for i in range(9):
#     sudoku_tbl.append([int(x) for x in input().split()])
# count = [0]
# back_track(sudoku_tbl, 0, 0)
# print(count[0])

###binary generation
# n = int(input())
# prev_text = ['0', '1']
# for i in range(2, n+1):
#     text = []
#     for seq in prev_text:
#         text.append('0' + seq)
#         text.append('1' + seq)
#     prev_text = text
# text.sort()
# print('\n'.join(text))