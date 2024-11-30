###ex1
# a, b = [int(x) for x in input().split()]
# print(a+b, a-b, a*b, a//b)

###ex2
# n = int(input())
# int_list = [int(x) for x in input().split()]
# _ = input()
# text = input()
# while text != '***':
#     if text == 'find-max':
#         print(max(int_list))
#     elif text == 'find-min':
#         print(min(int_list))
#     elif text == 'sum':
#         print(sum(int_list))
#     else:
#         _, x, y = text.split()
#         x, y = int(x), int(y)
#         print(max(int_list[x-1: y]))

#     text = input()

###ex3
# n = int(input())
# result = []
# for i in range(100, 1000):
#     if i%n == 0:
#         result.append(str(i))
# print(' '.join(result))

###ex4
# n = int(input())
# ints = [int(x) for x in input().split()]
# print(sum(ints))

###ex5
# text = ''
# while True:
#     try:
#         text += input() + '\n'
#     except:
#         break

# print(text.upper())
###ex6
# n, k = [int(x) for x in input().split()]
# ints = [int(x) for x in input().split()]
# weight = sum(ints[:k])
# if weight %2 == 0:
#     Q = 1
# else:
#     Q = 0
# for i in range(1, n-k+1):
#     weight += ints[i-1+k] - ints[i-1]
#     if weight %2 == 0:
#         Q += 1
# print(Q)

###ex7
# count = 0
# while True:
#     try:
#         count += len(input().split())
#     except:
#         break

# print(count)

###ex8
# P1 = input()
# P2 = input()
# T = input()
# while P1 in T:
#     T = T.replace(P1, P2)
# print(T)
