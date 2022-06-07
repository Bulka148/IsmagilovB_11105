import functools
import collections


def my_code_metod(string):
    res = ''
    for i in range(len(string)):
        if len(string) % 2 == 0:
            k = (ord(string[i]) - ord('а') + 33) % 32
        else:
            k = (ord(string[i]) - ord('а') + 31) % 32
        res += chr(k + ord('а'))
    return res


with open('text.txt', 'r', encoding='utf8') as file:
    my_list_1 = file.read().lower()
    my_list = my_list_1
    my_list = my_list.replace('–', '').replace('!', '').replace('?', '').replace('‑', ' ').replace(';', '').split()

with open('text.txt', 'a', encoding='utf8') as f:
    f.write('\n' + str(len(set(my_list))) + '\n')

    my_dict = {}
    for i in range(ord('а'), ord('я')+1):
        my_dict[chr(i)] = 0

    for word in my_list:
        if my_dict.get(word[0]) is not None:
            my_dict[word[0]] += 1

    for k in my_dict.keys():
        if my_dict[k] > 0:
            f.write(str(k + ':' + str(my_dict[k])) + '\n')

    lengths = map(lambda e: len(e), my_list)
    max_length = functools.reduce(lambda a, b: max(a, b), lengths)
    f.write(str([e for e in my_list if len(e) == max_length][0]) + '\n')

    first = lambda e: e[1]
    f.write(str(max(dict(collections.Counter(my_list)).items(), key=first)[0]) + '\n')