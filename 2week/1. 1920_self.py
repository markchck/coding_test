# 10시 37분에 시작 11시 37분에 마무리

# hashset을 사용해서 가장 빠른시간에 문제 풀었음.(최적의 풀이임)
# N=int(input())
# A=set(map(int, input().split(" ")))
# M=int(input())
# B=map(int, input().split(" "))

# for itr_B in B:
#   if(itr_B in A):
#     print(1)
#   else:
#     print(0)


# 그럼에도 이진탐색 연습용 풀이 해보자.
N= int(input())
A= list(map(int, input().split(" ")))
M= int(input())
B= list(map(int, input().split(" ")))

A.sort()


for itr_B in B:
  # 선형탐색은 시간이 오래걸리니 이진탐색으로가자
  left= 0
  right=N-1

  judge=0

  # 조건이 복잡한 반복문이니 while을 쓰자
  while left<=right:
    mid = (left+right)//2
    if A[mid] == itr_B:
      print(1)
      judge=1
      break
    elif(A[mid]>itr_B):
      right = mid-1
    else:
      left = mid+1
  if judge==0:
    print(judge)
  # 없으면 0을 출력하기 위해서 주가 로직이 필요하다.

# 와 계속 루프돌길래 뭔가 했더니...이진탐색의 전제조건 정렬을 안했네.. 이거 못풀었다.

# 와...while left<=right: 등호 안붙이면 A배열의 마지막 자리는 무조건 0이 나오네? (mid가 3이라 left도4(mid+1)로 rihgt는 (M-1이라서 4)
# 그럼 While문을 돌지 않아서 그냥 0이 출력.

# 대체 왜 런타임에러가 뜨냐? 
# 와..right=N-1 이걸 M-1이라고했음. 그래서 런타임 에러 뜸.