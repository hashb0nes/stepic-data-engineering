
import sys

lines = [line.rstrip() for line in sys.stdin]
p = int(lines[0])
n = int(lines[1])
messages = lines[2: 2 + n]

def round_robin(p, messages):
    result = [[] for _ in range(p)]
    for i, message in enumerate(messages):
        result[i % p].append(message)
    for line in result:
        print(' '.join(line))

round_robin(p, messages)