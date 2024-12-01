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

###Stack
# stack = []
# while True:
#     command = input()
#     if command == '#':
#         break

#     temp = command.split()
#     if len(temp) == 2 and temp[0] == 'PUSH':
#         stack.append(temp[1])
#     elif len(temp) == 1 and temp[0] == 'POP':
#         if len(stack) != 0:
#             print(stack[-1])
#             stack.pop()
#         else:
#             print('NULL')


###Tree
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.child = []

#     def insert(self, c_val, p_val):
#         if self.key == p_val:
#             new_child = Node(c_val)
#             self.child.append(new_child)
#             return 0
#         else:
#             for child in self.child:
#                 child.insert(c_val, p_val)

#     def preOrder(self):
#         if self != None:
#             print(self.key, end=' ')
#             for child in self.child:
#                 child.preOrder()

#     def inOrder(self):
#         if self != None:
#             if len(self.child) > 0:
#                 self.child[0].inOrder()
#                 print(self.key, end=' ')
#                 for child in self.child[1:]:
#                     child.inOrder()
#             else:
#                 print(self.key, end=' ')

#     def postOrder(self):
#         if self != None:
#             for child in self.child:
#                 child.postOrder()
#             print(self.key, end=' ')

# root = None
# while True:
#     command = input()
#     if command == '*':
#         break

#     temp = command.split()
#     if len(temp) == 2 and temp[0] == 'MakeRoot':
#         root = Node(int(temp[1]))
#     elif len(temp) == 3 and temp[0] == 'Insert':
#         root.insert(c_val=int(temp[1]), p_val=int(temp[2]))
#     elif len(temp) == 1:
#         if temp[0] == 'PreOrder':
#             root.preOrder()
#         if temp[0] == 'InOrder':
#             root.inOrder()
#         if temp[0] == 'PostOrder':
#             root.postOrder()

### Queue
# queue = []
# while True:
#     command = input()
#     if command == '#':
#         break

#     temp = command.split()
#     if len(temp) == 2 and temp[0] == 'PUSH':
#         queue.append(temp[1])
#     elif len(temp) == 1 and temp[0] == 'POP':
#         if len(queue) != 0:
#             print(queue[0])
#             queue.pop(0)
#         else:
#             print('NULL')