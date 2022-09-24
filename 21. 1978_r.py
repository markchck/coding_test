# https://www.acmicpc.net/problem/1978

def judge_prime_number(i):
  if(i==1):
    return None
  elif(i==2):
    return int(i)
  elif(i%2==0):
    return None
  else:
    # 3,5,7,9 같은 놈들에 대해 1부터 n-1 숫자로 나눠봄
    for a in range(i):
      b= a+1 # a는 0부터 시작하니까 1부터하게하려고 
      if(b== 1 or b== 2 or (b%2 ==0)):
        None
      else:
        if(i%b==0 and i!=b):
          return None
        else:
          None
          # print(f"{b} 루프다돌기전까진 {i}가 소수인지는 모르는겨")
    # print("여기까지 왔으면 넌 소수다")
    return int(i)

N = int(input())
A = list(map(int, input().split(" ")))
B =[]
for number in A:
  B.append(judge_prime_number(number))

C= []
for b in B:
  # print(b)
  if b != None:
    C.append(b)
print(len(C))