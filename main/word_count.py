import json
import re
from collections import defaultdict

input_data = input().strip()
input_json = json.loads(input_data)


def word_count(lines):
    result = {}

    for line in lines:
        words = re.findall(r'\b[a-zA-Z]+\b', line.lower())

        for word in words:
            if word:
                result[word] = result.get(word, 0) + 1

    return result


def word_count_split(lines):
    result = {}

    for line in lines:
        words = re.split(r'[\s\t\n]', line.lower())

        for word in words:
            if word:
                result[word] = result.get(word, 0) + 1

    return result


def word_count_simple_split(lines):
    result = defaultdict(int)
    for line in lines:
        for word in line.lower().split():
            result[word] += 1

    return dict(result)

print(word_count(input_json['lines']))
print(word_count_split(input_json['lines']))
print(word_count_simple_split(input_json['lines']))


# {"lines":["Hello World","hello kafka streams"]}
# {"lines":["Hello  ,  World   ","hello\tkafka streams! streams, streams"]}
# Ввод
# lines = ["Hello World", "hello kafka streams"]
#
# Вывод
# {
#   "hello": 2,
#   "world": 1,
#   "kafka": 1,
#   "streams": 1
# }