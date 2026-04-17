from typing import List
import json

# my first not optimal solution
def estimate_batches(sizes: List[int], batch_size: int, linger_ms: int):
    sizes_sorted = sorted(sizes)
    result = []
    while sizes_sorted:
        min_batch = []
        for i in range(len(sizes_sorted) -1, -1, -1):
            current_size = sizes_sorted[i]
            # if single size more than batch_size
            if current_size >= batch_size:
                min_batch.append(sizes_sorted.pop(i))
                break
            if sum(min_batch) + current_size <= batch_size:
                min_batch.append(sizes_sorted.pop(i))
        result.append(min_batch)
    return result

# classic First-Fit Decreasing
def estimate_batches_ffd(sizes: List[int], batch_size: int, linger_ms: int):
    sorted_sizes = sorted(sizes, reverse=True)

    batches: List[List[int]] = []
    batch_sum: List[int] = []

    for size in sorted_sizes:
        placed = False
        for i in range(len(batches)):
            if batch_sum[i] + size <= batch_size:
                batches[i].append(size)
                batch_sum[i] += size
                placed = True
                break

        if not placed:
            batches.append([size])
            batch_sum.append(size)

    return batches




input_str = input()
input_json = json.loads(input_str)

print(estimate_batches(input_json['sizes'], input_json['batch_size'], input_json['linger_ms']))
print(estimate_batches_ffd(input_json['sizes'], input_json['batch_size'], input_json['linger_ms']))



# Ввод
# {"sizes":[100,500,200,300,400],"batch_size":700,"linger_ms":50}
# sizes = [100, 500, 200, 300, 400]
# batch_size = 700
#
# Вывод
# 3
# [100, 500], [200, 300], [400].