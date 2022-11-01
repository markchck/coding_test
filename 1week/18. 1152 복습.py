# 문자열을 받고, SPLIT의 길이를 출력
# strip()은 앞 뒤 공백을 떼고 입력한 값 한줄을 통째로 배열에 넣고 
# split()은 입력한 값을 공백을 기준으로 나눠서 한 배열에 넣고
# strip().split()하면 공백 제거한거 통째로 한 배열에 넣고 공백 기준으로 나눈 것.


import sys
s = sys.stdin.readline().strip()
print(s)
print(s.count(" ")+1 if s else 0)
# strip으로 하면 앞 뒤 공백 떼고 나머지가 통짜로 한 배열에 들어오는구나
# 그걸 split으로 " "

# split을 할 필요가 없나본데?
# A = input().strip().split(" ")
# print(A)
# print(A[0] =="")
# if A[0]== "":
#   print(0)
# else:
#   print(len(A))