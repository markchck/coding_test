# https://www.acmicpc.net/problem/10872
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# n=0일수도 있다!!!

def multiple(n):
  if n==0:
    return 1
  else:
    return (multiple(n-1) * n)

n =int(input())
print(multiple(n))


# def multiple(a,b):
#   result = (a*b)
#   return result

# N = int(input())
# list = []
# for i in range(N):
#   new_i = i+1
#   list.append(new_i)

# a=0
# b=0
# for i in range(len(list)-2):
#   front = multiple(list[i], list[i+1])
#   result = multiple(front, list[i+2])
# print(result)
