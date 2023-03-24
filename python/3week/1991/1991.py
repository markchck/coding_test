#전위순위(DFS)
import sys
input = sys.stdin.readline
N =int(input())
tree = {} #딕셔너리 자료구조를 써야겠다고 생각하는게 중요한 포인트 중 하나일 듯
for i in range(N):
    root, l, r = (input().split())
    tree[root] = (l,r) 
# print(tree['A'])

def preOrder(root):
    if root != ".":
        print(root, end='')
        preOrder(tree[root][0])
        preOrder(tree[root][1])
preOrder('A')
print()

def midOrder(root):
    if root != '.':
        midOrder(tree[root][0])
        print(root, end='')
        midOrder(tree[root][1])
midOrder('A')
print()

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end='')
postOrder('A')
print()