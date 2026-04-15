import json

input_data = input().strip()
data = json.loads(input_data)

def rebalance(current_assignment, leaving_consumer):
    consumers = [k for k in current_assignment if k != leaving_consumer]
    if len(consumers) == 0:
        return {}

    partitions = [p for partition_list in current_assignment.values() for p in partition_list]
    result = {c: [] for c in consumers}

    for i, p in enumerate(partitions):
        result[consumers[i % len(consumers)]].append(p)

    return result


# print(rebalance({"c1":[0,3],"c2":[4,1],"c3":[5,2]}, "c2"))
print(rebalance(data['assignment'], data['leave']))


# Ввод
# current_assignment = {
#     "c1": [0, 3],
#     "c2": [1, 4],
#     "c3": [2, 5]
# }
# leaving_consumer = "c2"
#
# Вывод (один из вариантов)
# {
#     "c1": [0, 3, 1],
#     "c3": [2, 5, 4]
# }

# {"assignment":{"c1":[0,3],"c2":[4,1],"c3":[5,2]},"leave":"c2"}