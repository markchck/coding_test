# https://www.acmicpc.net/problem/2309
# 9개 숫자 다 더하고 100보다 얼마나 큰지 구하고 그 숫자를 B라하면
# B - 9개 숫자 하나씩 하고
# 차이값이 9개중 있으면 그 쌍은 배열에서 제외시켜주면 됨.

n_list = []
for i in range(9):
  n_list.append(int(input()))
total = sum(n_list)
diff = total-100
# print(diff)

# for i in range(len(n_list)):
#   target= diff-n_list[i]
#   if target in n_list:
#     del(n_list[i])

for i in n_list:
  target = diff-i
  if target != i:
    if (target in n_list):
      # del(target)
      n_list.remove(target)
      n_list.remove(i)
      break

result = sorted(n_list)
for i in result:
  print(i)
