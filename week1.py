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

##ex9
# import math
# a, b, c = (float(x) for x in input().split())
# delta = b*b - 4*a*c
# if delta < 0:
#     print('NO SOLUTION')
# elif delta == 0:
#     x0 = -b/(2*a)
#     print("%.2f" %x0)
# else:
#     x1 = (-b-math.sqrt(delta))/(2*a)
#     x2 = (-b+math.sqrt(delta))/(2*a)
#     print("%.2f %.2f" %(x1, x2))

###ex10
# try:
#     yyyy, mm, dd = input().split('-')
#     y, m, d = int(yyyy), int(mm), int(dd)
#     if 1<=m<=12 and 1<=d<=31 and len(yyyy)==4 and len(mm)==2 and len(dd)==2:
#         print(y, m, d)
#     else:
#         print('INCORRECT')
# except:
#     print('INCORRECT')

###ex11
# n = int(input())
# for i in range(1, n+1):
#     print(i, i*i)

###ex12
# odd, even = 0, 0
# n = int(input())
# ints = [int(x) for x in input().split()]
# for i in ints:
#     if i %2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(odd, even)


###ex13
# try:
#     hh, mm, ss = input().split(':')
#     h, m, s = int(hh), int(mm), int(ss)
#     if 0<=h<=23 and 0<=m<=59 and 0<=s<=59 and len(hh)==2 and len(mm)==2 and len(ss)==2:
#         print(h*3600 + m*60 + s)
#     else:
#         print('INCORRECT')
# except:
#     print('INCORRECT')

##ex14
# def step(a, b, k, x):
#     if b>0:
#         if x<a:
#             return 0
#         if x>b:
#             return k*(b-a)
#         else:
#             return k*(x-a)
#     else:
#         if x<a:
#             return 0
#         else:
#             return k*(x-a)
# def old(x):
#     result = 0
#     result += step(0,   50,  1728, x)
#     result += step(50,  100, 1786, x)
#     result += step(100, 200, 2074, x)
#     result += step(200, 300, 2612, x)
#     result += step(300, 400, 2919, x)
#     result += step(400, -1,  3015, x)
#     return result
# def new(x):
#     result = 0
#     result += step(0,   100, 1728, x)
#     result += step(100, 200, 2074, x)
#     result += step(200, 400, 2612, x)
#     result += step(400, 700, 3111, x)
#     result += step(700, -1,  3457, x)
#     return result

# x = int(input())
# diff = 1.1 * (new(x) - old(x))
# print("%.2f" %diff)