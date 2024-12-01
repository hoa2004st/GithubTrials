##### Cityzen Data Analysis
# import sys
# input = sys.stdin.read
# output = sys.stdout.write
# from collections import defaultdict

# def count_people():
#     return len(database)
# def count_people_born_at(date):
#     return sum(1 for person in database if person[1] == date)
# def most_alive_ancestor(code):
#     code_map = {person[0]: person for person in database}
#     def ancestor_depth(code):
#         if code == '0000000' or code not in code_map:
#             return 0
#         father = code_map[code][2]
#         mother = code_map[code][3]
#         return 1 + max(ancestor_depth(father), ancestor_depth(mother))
#     return ancestor_depth(code) - 1
# def count_people_born_between(from_date, to_date):
#     return sum(1 for person in database if from_date <= person[1] <= to_date)
# def max_unrelated_people():
#     code_map = {person[0]: person for person in database}
#     parent_child_graph = defaultdict(set)

#     for person in database:
#         code = person[0]
#         father = person[2]
#         mother = person[3]
#         if father != '0000000':
#             parent_child_graph[father].add(code)
#             parent_child_graph[code].add(father)
#         if mother != '0000000':
#             parent_child_graph[mother].add(code)
#             parent_child_graph[code].add(mother)

#     visited = set()
#     color = {}

#     def bfs(node):
#         queue = [node]
#         color[node] = 0 
#         color_count = [0, 0] 
#         color_count[0] += 1
        
#         while queue:
#             current = queue.pop(0)
#             current_color = color[current]
            
#             for neighbor in parent_child_graph[current]:
#                 if neighbor not in color:
#                     color[neighbor] = 1 - current_color
#                     color_count[1 - current_color] += 1
#                     queue.append(neighbor)
        
#         return max(color_count)

#     max_subset_size = 0

#     for person in code_map:
#         if person not in color:
#             max_subset_size += bfs(person)

#     return max_subset_size


# database = []
# results = []

# input_lines = input().strip().splitlines()

# i = 0
# while input_lines[i] != '*':
#     database.append(input_lines[i].split())
#     i += 1

# i += 1

# while input_lines[i] != '***':
#     query = input_lines[i].split()
#     if query[0] == 'NUMBER_PEOPLE':
#         results.append(count_people())
#     elif query[0] == 'NUMBER_PEOPLE_BORN_AT':
#         results.append(count_people_born_at(query[1]))
#     elif query[0] == 'MOST_ALIVE_ANCESTOR':
#         results.append(most_alive_ancestor(query[1]))
#     elif query[0] == 'NUMBER_PEOPLE_BORN_BETWEEN':
#         results.append(count_people_born_between(query[1], query[2]))
#     elif query[0] == 'MAX_UNRELATED_PEOPLE':
#         results.append(max_unrelated_people())
#     i += 1

# print('\n'.join(map(str, results)))




##### Analize Code Submission

# import sys
# input = sys.stdin.read
# output = sys.stdout.write
# from collections import defaultdict

# def total_number_submissions():
#     return len(submissions)

# def number_error_submission():
#     return sum(1 for submission in submissions if submission[3] == 'ERR')

# def number_error_submission_of_user(user_id):
#     return sum(1 for submission in submissions if submission[3] == 'ERR' and submission[0] == user_id)

# def total_point_of_user(user_id):
#     points = {}
#     for submission in submissions:
#         if submission[0] == user_id and submission[3] == 'OK':
#             problem_id = submission[1]
#             point = int(submission[4])
#             if problem_id not in points or points[problem_id] < point:
#                 points[problem_id] = point
#     return sum(points.values())

# def number_submission_period(from_time, to_time):
#     return sum(1 for submission in submissions if from_time <= submission[2] <= to_time)


# submissions = []
# results = []
# input_lines = input().strip().splitlines()

# i = 0
# while input_lines[i] != '#':
#     submissions.append(input_lines[i].split())
#     i += 1

# i += 1

# while input_lines[i] != '#':
#     query = input_lines[i].split()
#     if query[0] == '?total_number_submissions':
#         results.append(total_number_submissions())
#     elif query[0] == '?number_error_submision':
#         results.append(number_error_submission())
#     elif query[0] == '?number_error_submision_of_user':
#         results.append(number_error_submission_of_user(query[1]))
#     elif query[0] == '?total_point_of_user':
#         results.append(total_point_of_user(query[1]))
#     elif query[0] == '?number_submission_period':
#         results.append(number_submission_period(query[1], query[2]))
#     i += 1

# print('\n'.join(map(str, results)))





