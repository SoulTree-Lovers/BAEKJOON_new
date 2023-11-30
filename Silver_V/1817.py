# 짐 챙기는 숌

n, m = map(int, input().split()) # 책의 개수, 박스에 넣을 수 있는 최대 무게

# 책이 없는 경우 0 출력
if n == 0:
    print(0)
    exit()

books = list(map(int, input().split())) # 책의 무게

box_count = 0 # 필요한 박스 개수

while books:
    remain_box_weight = m # 박스에 넣을 수 있는 무게
    box_count += 1 # 박스 개수 증가

    # 박스에 담을 수 있는 만큼 넣기 
    while books:
        if remain_box_weight >= books[0]:
            remain_box_weight -= books.pop(0)
        else:
            break

print(box_count)