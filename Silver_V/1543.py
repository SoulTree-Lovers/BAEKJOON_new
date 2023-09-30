# 문서 검색
import sys
input = sys.stdin.readline

string = input().strip()
find = input().strip()

temp = string.replace(find, "")

print(int((len(string) - len(temp)) / len(find)))

