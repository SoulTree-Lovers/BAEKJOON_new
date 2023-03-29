# 문자열 폭발

def explode_string(s, bomb):
    stack = []  # stack to keep track of the remaining characters after explosions
    
    for char in s:
        stack.append(char)  # add current character to stack
        
        # check if the bomb string is present in the stack
        if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
            # if bomb string is present, remove it from stack
            del stack[-len(bomb):]
            
    result = ''.join(stack)  # concatenate the remaining characters
    
    if not result:  # if no remaining characters, return "FRULA"
        return "FRULA"
    
    return result


# example usage
s = input().strip()
bomb = input().strip()

result = explode_string(s, bomb)
print(result)
