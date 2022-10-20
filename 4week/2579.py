N =int(input())
# 못풀었습니다.

# 내계획.
# n번째 시점에서 2칸 뛸지, 1칸 뛸지만 정하면 된다.
# n번까지 선택이 이미 최적이었다고 치고, 다음에 뛸 때, 2칸 뛸때의 점수랑, 1칸 뛸때의 점수 중 큰 놈이 n+1번째가 된다.
# max_step을 넘지 않을때까지 dfs로 탐색을 하고 dp테이블을 갱신한다. (행은 스탭수, 열을 계단의 인덱스, dp[1][1]은 10점)
# 갱신을 마친 dp테이블에서 max_step의 값을 정답으로 출력한다.

stairs = [0]*(N+1)
for i in range(1,N+1):
  stairs[i] = int(input())

# 최대 움직일 수 있는 횟수 = (N - (N//3))
max_step = N-(N//3)

dp=[ [0]*(N+1) for _ in range(max_step) ]

def dfs(r,c):
  for r in range(1, max_step+1): #0번스탭, 1번 스탭,2,3,4번스탭 
    for c in range(1, len(stairs)): #0번계단, 1번 계단,,,,
      #연속해서 3계단 뛰었는지 체크
        
      #아니면 이거 해도 됨.
      dp[r][c] = max ( dp[r][c], dfs(r-1,c-1) )

dfs(0,0) #0번 스탭, 0번 계단에서 시작