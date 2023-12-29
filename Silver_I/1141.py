# 접두사

n = int(input())

strings = list()

for i in range(n):
    strings.append(input())

strings.sort(key=lambda x: len(x))  # 길이별로 정렬

temp_strings = strings.copy()

for i in range(len(strings)):
    item = strings[i]
    for j in range(i+1, len(strings)):
        if item == strings[j][:len(item)]:  # 접두사가 일치하는 항목 찾기
            # print("strings[i][:len(item)]: ", strings[j][:len(item)])
            # print("item: ", item)
            temp_strings.remove(item)
            break


print(len(temp_strings))