# 백준 2110공유기를 푸는데
# count변수를 전역적으로 선언하고 루프를들어갔다.
# 그랬더니 틀림. 아래 코드를 보고 무슨 count를 루프 밖에 선언하는 것과 안에 선언하는 것이 무슨 차이인지 설명해봐

# def BOJ2110():
#   count = 1  #1번 경우 :count를 루프 밖에서 선언하는 상황
#   while(min <= max):
#     count =1 #2번 경우 :count를 루프 안에서 선언하는 상황
#     (count에 1을 더해주는 로직)

# BOJ2110()

# 밖에서 선언하면 while도는 횟수만큼 +1씩 되어서 count가 누적되고
# 안에서 선언하면 while문 돌때마다 count는 1로 갱신된다. 




