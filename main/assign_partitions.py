
def assign_partitions(num_partitions: int, consumer_ids: list[str]):
    result = {c: [] for c in consumer_ids}

    for p in range(num_partitions):
        result[consumer_ids[p % len(consumer_ids)]].append(p)

    return result

n = int(input())
c = input().split(' ')

print(assign_partitions(n, c))




#
# Ввод
# num_partitions = 5
# consumer_ids = ["c1", "c2", "c3"]
#
# Вывод (один из вариантов)
# {
#     "c1": [0, 3],
#     "c2": [1, 4],
#     "c3": [2]
# }