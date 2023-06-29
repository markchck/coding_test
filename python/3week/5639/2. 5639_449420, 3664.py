# 전위 순회를 후위순위로 바꾸는 문제
# 1. 입력을 동적으로 받아야함
# 2. 재귀적으로 호출이 일어나야하기 때문에 함수 정의가 필요함
# 3. 루트와 어디까지가 왼쪽 서브트리이고 어디까지가 오른쪽 서브트리인지 정의해줘야함
# 4. 후위순위이기 때문에 왼쪽, 오른쪽, 루트 순으로 print 해주면 된다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

preOrder = []

# 1. 입력을 동적으로 받아야함
while True:
    try:
        preOrder.append(int(input()))
    except:
        break


def dfs(array):
    # 2. 재귀적으로 호출이 일어나야하기 때문에 함수 정의가 필요함
    left, right = [], []

    if len(array) == 0:
        return

# 3. 루트와 어디까지가 왼쪽 서브트리이고 어디까지가 오른쪽 서브트리인지 정의해줘야함
    root = array[0]
    for i in range(1, len(array)):
        if array[i] < root:
            left.append(array[i])
        else:
            right.append(array[i])

# 4. 후위순위이기 때문에 왼쪽, 오른쪽, 루트 순으로 print 해주면 된다.
    dfs(left)
    dfs(right)
    print(root)


dfs(preOrder)
