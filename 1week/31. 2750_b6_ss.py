# https://www.acmicpc.net/problem/2750
# 파이썬 내장함수 sort 사용 
# 내장함수랑 sort함수 시간 복잡도 비교했더니 sort가 더 빠르다!! => sort함수는 이미 최적화 오지게 된 알고리즘이니 가져다 쓰자.
# https://blog.naver.com/hjy5405/222602862537

#sort함수로 풀어볼 것!
N = int(input())
number_list=[]
for i in range(N):
  number = int(input())
  number_list.append(number)
a=sorted(number_list)
print(a)
