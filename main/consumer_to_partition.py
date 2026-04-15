

n = int(input())
c = input().rstrip().split(' ')
p = int(input())
result = {i: [] for i in c}

for i in range(p):
    result[c[i % n]].append(i)

print(result)


# 3
# c1 c2 c3
# 5
#
# {'c1': [0, 3], 'c2': [1, 4], 'c3': [2]}