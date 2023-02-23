# 짝수가 아니면 False
# (개수랑 )개수가 안맞으면 False

# 이걸 먼저 짜면 될 듯
#()짝이 맞으면 Pop, 뭔가 남으면 False


import sys
input = sys.stdin.readline
N=int(input())

for _ in range(N):
    VPS=input().strip()
    list_a=[]
    for itr in VPS:
        if itr == '(':
            list_a.append(itr)
        elif itr == ')':
            #list_a에 (가 있는 경우
            if len(list_a)>0:        
                list_a.pop()
            #list_a에 (가 없는 경우
            elif len(list_a) == 0:
                list_a.append(itr)
                break
    if len(list_a) == 0:
        print('YES')  
    else:
        print('NO')



# import sys
# input = sys.stdin.readline
# N=int(input())

# for _ in range(N):
#     VPS=input().strip()
#     list_a=[]
#     for itr in VPS:
#         if itr == '(':
#             list_a.append(itr)
#         elif itr == ')':
#             #list_a에 (가 있는 경우
#             if len(list_a)>0:        
#                 list_a.pop()
#             #list_a에 (가 없는 경우
#             elif len(list_a) == 0:
#                 print('NO')
#                 continue
#     if len(list_a) == 0:
#         print('YES')  
#     else:
#         print('NO')
