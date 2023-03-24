# 자릿수로 쪼개는 방법

# 등차수열인지 확인하는 방법


number = int(input())
hansu = 0
for num in range(1, number+1):
  if num <=99:
    hansu+=1
  else:
    splited_num=list(map(int, str(num)))
    if splited_num[0]-splited_num[1] == splited_num[1]-splited_num[2]:
      hansu+=1
print(hansu)


    