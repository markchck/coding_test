# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    A.sort()
    length = len(A)
    for i in range(length):
        if(A[i]) > length:
            new_A = A[0:i]
        else:
            new_A = A
    
    list_a = [0] * (new_A[-1] +1) 
    for i in range(len(new_A)):
        order= new_A[i]
        list_a[order] += 1
    
    result = []
    for i in range(1, len(list_a)):
        if i == list_a[i]:
            result.append(i)
        else:
            continue

    if len(result) !=0:
        return max(result)
    else:
        return 0
