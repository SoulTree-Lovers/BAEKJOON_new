# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemons_name = {}
pokemons_index = {}

for i in range(n):
    data = input().strip()
    pokemons_index[i + 1] = data
    pokemons_name[data] = i + 1

# print(pokemons)

output = []

for i in range(m):
    order = input().strip()

    if order.isdigit():
        output.append(pokemons_index[int(order)])
        
    else:
        output.append(pokemons_name[order])
        

for i in output:
    print(i)