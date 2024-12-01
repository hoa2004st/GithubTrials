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

### Water Jug
# a, b, c = [int(x) for x in input().split()]

# class Action:
#     def check(self, jug_a, jug_b):
#         return True

#     def act(self, jug_a, jug_b):
#         return 0, 0


# class full_a(Action):
#     def check(self, jug_a, jug_b):
#         return jug_a != a

#     def act(self, jug_a, jug_b):
#         return a, jug_b


# class full_b(Action):
#     def check(self, jug_a, jug_b):
#         return jug_b != b

#     def act(self, jug_a, jug_b):
#         return jug_a, b


# class a_to_b(Action):
#     def check(self, jug_a, jug_b):
#         return jug_a > 0 and jug_b < b

#     def act(self, jug_a, jug_b):
#         transfer = min(jug_a, b - jug_b)
#         return jug_a - transfer, jug_b + transfer


# class b_to_a(Action):
#     def check(self, jug_a, jug_b):
#         return jug_b > 0 and jug_a < a

#     def act(self, jug_a, jug_b):
#         transfer = min(jug_b, a - jug_a)
#         return jug_a + transfer, jug_b - transfer


# class empty_a(Action):
#     def check(self, jug_a, jug_b):
#         return jug_a != 0

#     def act(self, jug_a, jug_b):
#         return 0, jug_b


# class empty_b(Action):
#     def check(self, jug_a, jug_b):
#         return jug_b != 0

#     def act(self, jug_a, jug_b):
#         return jug_a, 0


# actions = [full_a(), a_to_b(), empty_a(), full_b(), b_to_a(), empty_b()]

# def bfs():
#     queue = [(0, 0, 0)]  # Each element is (jug_a, jug_b, steps)
#     visited = []

#     while queue:
#         jug_a, jug_b, steps = queue.pop(0)

#         if jug_a == c or jug_b == c:
#             print(steps)
#             return True

#         if (jug_a, jug_b) in visited:
#             continue
#         visited.append((jug_a, jug_b))

#         for action in actions:
#             if action.check(jug_a, jug_b):
#                 next_a, next_b = action.act(jug_a, jug_b)
#                 if (next_a, next_b) not in visited:
#                     queue.append((next_a, next_b, steps + 1))

#     return False

# bfs()

### Family Tree

# class Node:
#     community = []
#     def __init__(self, parent, name):
#         Node.community.append(self)
#         self.parent = parent #Node Object
#         self.name = name #String Object
#         self.child = [] #List of Nodes

#     def insert(child_name, parent_name): #Node, String, String
#         child, parent = None, None
#         for person in Node.community:
#             if person.name == parent_name:
#                 parent = person
#             elif person.name == child_name:
#                 child = person
#         if parent == None:
#             parent = Node(None, parent_name)
#         if child == None:
#             child = Node(None, child_name)
#         parent.child.append(child)
#         child.parent = parent
#         # print(len(Node.community))


#     def des(parent):
#         result = 0
#         if len(parent.child) != 0:
#             for c in parent.child:
#                 result = result + 1 + c.des()
#         return result
#     def gen(parent):
#         result = 0
#         if len(parent.child) != 0:
#             for c in parent.child:
#                 result = 1 + c.gen()
#         return result

# while True:
#     command = input()
#     if command == '***':
#         break
#     temp = command.split()
#     if len(temp) == 2:
#         Node.insert(temp[0], temp[1])

# while True: 
#     command = input()
#     if command == '***':
#         break
#     temp = command.split()
#     if len(temp) == 2:
#         if temp[0] == 'descendants':
#             for p in Node.community:
#                 if p.name == temp[1]:
#                     print(p.des())
#         elif temp[0] == 'generation':
#             for p in Node.community:
#                 if p.name == temp[1]:
#                     print(p.gen())