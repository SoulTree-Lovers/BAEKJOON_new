# 가장 긴 바이토닉 부분 수열

def bitonic_sequence_length(n, a):
    # initialize the arrays for increasing and decreasing sub-sequences
    increasing = [1] * n
    decreasing = [1] * n
    
    # find the length of the increasing sub-sequence
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and increasing[i] < increasing[j] + 1:
                increasing[i] = increasing[j] + 1
                
    # find the length of the decreasing sub-sequence
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if a[i] > a[j] and decreasing[i] < decreasing[j] + 1:
                decreasing[i] = decreasing[j] + 1
    
    # find the maximum length of bitonic sequence
    bitonic_seq_length = 0
    for i in range(n):
        bitonic_seq_length = max(bitonic_seq_length, increasing[i] + decreasing[i] - 1)
        
    return bitonic_seq_length

# read input values
n = int(input())
a = list(map(int, input().split()))

# call the function to find the length of longest bitonic sub-sequence
print(bitonic_sequence_length(n, a))
