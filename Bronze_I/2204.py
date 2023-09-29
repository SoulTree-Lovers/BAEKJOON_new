# 도비의 난독증 테스트
import sys
input = sys.stdin.readline


while 1:
    n = int(input())

    if n == 0:
        break
    
    curr_dict = dict()

    for i in range(n):
        temp = input().strip()
        curr_dict[temp.lower()] = temp


    curr_dict = sorted(curr_dict.items())
    
    print(curr_dict[0][1])
    
    

    