##### Analyze sales order
# import sys
# from bisect import bisect_left, bisect_right

# input = sys.stdin.read
# output = sys.stdout.write

# def time_to_sec(time):
#     h, m, s = map(int, time.split(':'))
#     return 3600 * h + 60 * m + s

# db = []
# total_orders = 0
# total_revenue = 0
# shop_revenue = {}
# customer_shop_revenue = {}

# data = input().splitlines()

# i = 0
# while data[i] != "#":
#     c_id, p_id, price, s_id, time = data[i].split()
#     price = int(price)
#     sec = time_to_sec(time)
#     db.append([c_id, p_id, price, s_id, sec])
    
#     total_orders += 1
#     total_revenue += price
    
#     if s_id not in shop_revenue:
#         shop_revenue[s_id] = 0
#     shop_revenue[s_id] += price
    
#     if c_id not in customer_shop_revenue:
#         customer_shop_revenue[c_id] = {}
#     if s_id not in customer_shop_revenue[c_id]:
#         customer_shop_revenue[c_id][s_id] = 0
#     customer_shop_revenue[c_id][s_id] += price

#     i += 1

# db.sort(key=lambda x: x[4])

# cumulative_revenue = []
# current_sum = 0
# for record in db:
#     current_sum += record[2]
#     cumulative_revenue.append(current_sum)

# i += 1
# res = []

# while data[i] != "#":
#     command = data[i].split()
    
#     if command[0] == '?total_number_orders':
#         res.append(f"{total_orders}\n")
    
#     elif command[0] == '?total_revenue':
#         res.append(f"{total_revenue}\n")
    
#     elif command[0] == '?revenue_of_shop':
#         shop_id = command[1]
#         res.append(f"{shop_revenue.get(shop_id, 0)}\n")
    
#     elif command[0] == '?total_consume_of_customer_shop':
#         customer_id = command[1]
#         shop_id = command[2]
#         if customer_id in customer_shop_revenue and shop_id in customer_shop_revenue[customer_id]:
#             res.append(f"{customer_shop_revenue[customer_id][shop_id]}\n")
#         else:
#             res.append("0\n")
    
#     elif command[0] == '?total_revenue_in_period':
#         start_time = time_to_sec(command[1])
#         end_time = time_to_sec(command[2])
        
#         start_idx = bisect_left([rec[4] for rec in db], start_time)
#         end_idx = bisect_right([rec[4] for rec in db], end_time) - 1
        
#         if start_idx <= end_idx:
#             result = cumulative_revenue[end_idx]
#             if start_idx > 0:
#                 result -= cumulative_revenue[start_idx - 1]
#             res.append(f"{result}\n")
#         else:
#             res.append("0\n")
    
#     i += 1

# output("".join(res))

#####Bank Transaction

import sys
input = sys.stdin.read
output = sys.stdout.write
from collections import defaultdict

def find_cycle(graph, start, k, current, visited, path_length):
    if path_length == k:
        return current == start
    
    visited.add(current)
    for neighbor in graph[current]:
        if (neighbor != start and neighbor not in visited) or (neighbor == start and path_length == k - 1):
            if find_cycle(graph, start, k, neighbor, visited, path_length + 1):
                return True
    visited.remove(current)
    return False


transactions = []
account_money_from = defaultdict(int)
all_accounts = set()
graph = defaultdict(list)

input_lines = input().strip().splitlines()

i = 0
while input_lines[i] != '#':
    from_acc, to_acc, money, time_point, atm = input_lines[i].split()
    money = int(money)
    transactions.append((from_acc, to_acc, money, time_point, atm))
    account_money_from[from_acc] += money
    all_accounts.add(from_acc)
    all_accounts.add(to_acc)
    graph[from_acc].append(to_acc)
    i += 1

i += 1

while input_lines[i] != '#':
    query = input_lines[i].split()

    if query[0] == "?number_transactions":
        output(f"{len(transactions)}\n")

    elif query[0] == "?total_money_transaction":
        total_money = sum(money for _, _, money, _, _ in transactions)
        output(f"{total_money}\n")

    elif query[0] == "?list_sorted_accounts":
        sorted_accounts = sorted(all_accounts)
        output(" ".join(sorted_accounts) + "\n")

    elif query[0] == "?total_money_transaction_from":
        account = query[1]
        output(f"{account_money_from[account]}\n")

    elif query[0] == "?inspect_cycle":
        account = query[1]
        k = int(query[2])
        visited = set()
        if find_cycle(graph, account, k, account, visited, 0):
            output("1\n")
        else:
            output("0\n")

    i += 1
