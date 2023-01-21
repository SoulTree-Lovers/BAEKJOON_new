# 스택

n = int(input())

stack = []

def push(stack, x):
    stack.insert(0, x)

def pop(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack.pop(0)

def size(stack):
    return len(stack)

def empty(stack):
    return 1 if len(stack) == 0 else 0

def top(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack[0]

print_list = []

for i in range(n):
    order = input().split()

    if order[0] == 'push':
        push(stack, order[1])
    
    elif order[0] == 'pop':
        print_list.append(pop(stack))
    
    elif order[0] == 'size':
        print_list.append(size(stack))
    
    elif order[0] == 'empty':
        print_list.append(empty(stack))
    
    elif order[0] == 'top':
        print_list.append(top(stack))
    
for i in print_list:
    print(i)