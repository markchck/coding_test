import sys
input = sys.stdin.readline

N = int(input())
word_list = []

for i in range(N):
    word = input().rstrip()
    word_list.append(word)

word_list = list(set(word_list))
print(word_list)

word_list.sort(key = lambda x : (len(x), x) )
for w in word_list:
    print(w)
