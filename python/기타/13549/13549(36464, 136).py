from collections import deque
n, k = map(int, input().split())
max = 100001
visited = [False]*max  # 방문체크0
dist = [0]*max  # 소요 시간 저장

que = deque()
que.append(n)
visited[n] = True


def bfs():
    while que:
        now = que.popleft()
        if now == k:
            return
        if 0 <= 2*now < max and not visited[2*now]:
            next = 2*now
            dist[next] = dist[now]  # 순간이동은 0초 걸리니까 now랑 시간이 같다.
            visited[next] = True
            que.append(next)
        if 0 <= now-1 < max and not visited[now-1]:
            next = now-1
            dist[next] = dist[now]+1
            visited[next] = True
            que.append(next)
        if 0 <= now+1 < max and not visited[now+1]:
            next = now+1
            dist[next] = dist[now]+1
            visited[next] = True
            que.append(next)


bfs()
print(dist[k])
