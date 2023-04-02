# Who is in the middle?

bowl = []

for i in range(3):
    bowl.append(int(input()))

bowl.sort()
print(bowl[1])