# 단어 공부 
import operator

word = input().upper()

word_dic = {}

for w in word:
    if w not in word_dic:
        word_dic[w] = 1
    else:
        word_dic[w] += 1


count_list = sorted(word_dic.values())

# print(count_list)
if len(count_list) > 1 and count_list[-1] == count_list[-2]:
    print("?")

else:
    print(max(word_dic.items(), key=operator.itemgetter(1))[0])


