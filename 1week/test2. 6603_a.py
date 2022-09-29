# https://www.acmicpc.net/problem/6603
input = list(map(int, input().split(" ")))
N= input[0]
numbers_list = input[1:]

lotto_list=[]
for i in range(0,N-5):
  tmp=[]
  A = numbers_list[i]
  tmp.append(A)
  for j in range(i+1,N-4):
    B = numbers_list[j]
    tmp.append(B)
    for k in range(j+1,N-3):
      C = numbers_list[k]
      tmp.append(C)
      for l in range(k+1,N-2):
        D = numbers_list[l]
        tmp.append(D)
        for m in range(l+1,N-1):
          E = numbers_list[m]
          tmp.append(E)
          for n in range(m+1,N):
            F = numbers_list[n]
            tmp.append(F)
            
            # tmp.append(F)
          lotto_list.append(tmp)


# print(tmp)
print(lotto_list)
# for l in lotto_list:
#   print(l)
# print(len(lotto_list))
  

