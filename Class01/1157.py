# 단어 공부

word = input().upper()

max_count = 0
max_word = None
count_list = []

for i in range(len(word)):
    word_count = word.count(word[i])

    if max_count < word_count:
        max_count = word_count
        max_word = word[i]
    
    count_list.append(word_count)

count_list.sort()

if count_list[-1] == count_list[-2]:
    print("?")

else:
    print(max_word)
    


        
