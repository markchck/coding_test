import heapq


def dijkstra(start, end):
    global nodes, length
    # cost를 기록할 기록지
    visit = [10**15]*(length+1)
    visit[start] = 0
    hq = []
    heapq.heappush(hq, [visit[start], start])

    while hq:
        cost, now = heapq.heappop(hq)
        if cost > visit[now]:
            continue
        for node in nodes[now]:
            new_cost, new = node
            new_cost += cost
            if new_cost < visit[new]:
                visit[new] = new_cost
                heapq.heappush(hq, [new_cost, new])
    return visit[end]


def solution(n, s, a, b, fares):
    global nodes, length
    # 관계설정
    # 최대값을 초기값으로 하고 더 작은 answer가 발견되면 갱신하는 방식 (다익스트라)
    # 재귀(특정 지점까지 가는 최소 비용 + 그 지점에서 a집가는 최소 비용 + 그 지점에서 b집가는 최소 비용)
    nodes = [[] for _ in range(n+1)]
    answer = 10**15
    length = n

    # 관계설정
    for fare in fares:
        start, end, cost = fare[0], fare[1], fare[2]
        nodes[start].append([cost, end])
        nodes[end].append([cost, start])

    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i)+dijkstra(i, a)+dijkstra(i, b))
    print(answer)
    return answer


solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
         5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
