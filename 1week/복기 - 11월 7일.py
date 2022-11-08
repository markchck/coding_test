# 마디별로 계산하기 로직 연습할 것
# 강한자만 살아남기 로직 연습

col, row = map(int, input().split())
count = int(input())
tmp_row=[0,row]
tmp_col=[0,col]

for _ in range(count):
  a,b = map(int, input().split())

  if a == 0:
    tmp_row.append(b)
  else:
    tmp_col.append(b)

 
tmp_row.sort()
tmp_col.sort()

result = []
# 마디별로 계산하기 로직
for i in range(len(tmp_row)-1):
  for j in range(len(tmp_col)-1):
    r = tmp_row[i+1] - tmp_row[i]
    c = tmp_col[j+1] - tmp_col[j]
    # 강한자만 살아남게 하는 로직
    # result = max(result, r*c)
    result.append(r*c)
print(result)