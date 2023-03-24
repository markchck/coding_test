# 굳이 정답 배열을 안 만들고 바로 출력할 수 있구나
# count함수를 사용해서 찾을 수 있구나

d= input
a = int(d())*int(d())*int(d())
a = str(a)
for i in range(10):
  print(a.count(str(i)))




# # 세개를 곱하고
# # 카운트 변수를 하나 만들고
# # 포문 돌려서 1부터 증가하며 1인 것 체크

# # 배열의 길이만큼 도는 루프하나랑
# # 1~9까지 도는 루프 하나 

# A= int(input())
# B= int(input())
# C= int(input())

# result = str(A*B*C)
# len_result=len(result)
# count=0
# # 0부터 시작 len_result :7이면
# for i in range(len_result):
#   while (i == len(len_result)-1):
#     if result[i] == 1:
#       count+=1
#     i+=1
#   print(count)
