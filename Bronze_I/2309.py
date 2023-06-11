# 일곱 난쟁이

nanjangs = []
num_list = []

for _ in range(9):
    nanjangs.append(int(input()))

for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    for f in range(9):
                        for g in range(9):
                            if a != b and a!= c and a!= d and a!= e and a!= f and a!= g and b!= c and b!= d and b!= e and b!= f and b!= g and c!= d and c!= e and c!= f and c!= g and d!= e and d!= f and d!= g and e!= f and e!= g and f!= g:
                                if nanjangs[a]+nanjangs[b]+nanjangs[c]+nanjangs[d]+nanjangs[e]+nanjangs[f]+nanjangs[g] == 100:
                                    num_list = [nanjangs[a], nanjangs[b], nanjangs[c], nanjangs[d], nanjangs[e], nanjangs[f], nanjangs[g]]
                                
for i in sorted(num_list):
    print(i)