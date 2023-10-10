# 균형잡힌 세상
import sys
# input = sys.stdin.readline

open_brackets = ["(", "["]
close_brackets = [")", "]"]

brackets = {"(" : ")", "[" : "]"}

while True:
    stack = []
    string = input()
    isBalanced = True

    if (string == "."):
        break

    for i in string:
        # print("stack: ", stack)
        # print("i: ", i)
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            if len(stack) > 0 and brackets[stack[-1]] == i:
                stack.pop()
                # print("stack: ", stack)
            else:
                isBalanced = False
                break
            
    if len(stack) > 0:
        isBalanced = False
    
    print("yes" if isBalanced else "no")
