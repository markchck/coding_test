# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# #BA를 카운팅
# def solution(S):
#     # Implement your solution here
    
#     count = 0

#     while S.find("BA") >= 0:
#         order = S.find("BA")
#         S = S[0 : order] + S[order+2:len(S)]
#         count +=1
#     return count



def solution(S):
    # Implement your solution here
    count = 0
    # while S.find('BA') != -1:
    if(S.find('BA') !=-1):
        S = S.replace('BA', '')
        # S.replace('BA', '') replace는 S를 받고 AABAB를 뱉는데 이걸 재할당을 안하고 그냥 S를 불러서 BAAABAB가 출력됐군..
        count+=1
        print(S)
    return print(count)
solution('BAAABAB')
