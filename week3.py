###Check parenthesis
# result = 1
# pars = input()
# close = {')':'(', ']':'[', '}':'{'}
# temp = []
# for p in pars:
#     if p not in close:
#         temp.append(p)
#     elif len(temp) == 0:
#         result = 0
#     elif temp[-1] == close[p]:
#         temp = temp[:-1]
#     else:
#         result = 0
# if len(temp) != 0:
#     result = 0
# print(result)