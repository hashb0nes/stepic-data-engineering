

count = int(input())
sizes = [int(x) for x in input().split(' ')]
batch_max_size = int(input())
send_times = [int(x) for x in input().split(' ')]
linger_ms = int(input())

if count == 0:
    print(0)
else:
    batch_count = 1
    first_ms = int(send_times[0])
    batch_size = int(sizes[0])

    for i in range(1, count):
        if batch_size + int(sizes[i]) > batch_max_size or int(send_times[i]) - first_ms > linger_ms:
            batch_count += 1
            batch_size = int(sizes[i])
            first_ms = int(send_times[i])
        else:
            batch_size += int(sizes[i])

    print(batch_count)








# Ввод
# 5
# 200 100 150 400 50
# 500
# 0 10 30 300 305
# 50
#
# Вывод
# 2


# Ввод
# 4
# 50 51 100 50
# 200
# 0 10 15 20
# 50
#
# Вывод
# 2