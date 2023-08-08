import heapq


def solution(n, costs):
    nodes = [[] for _ in range(n)]
    visited = [0] * (n)
    # 관계를 설정하고
    for cost in costs:
        start, end, cost = cost
        nodes[start].append((cost, end))
        nodes[end].append((cost, start))

    # [[(1, 1), (2, 2)], [(1, 0), (5, 2), (1, 3)], [(2, 0), (5, 1), (8, 3)], [(1, 1), (8, 2)], []]
    que = nodes[0]
    visited[0] = 1
    heapq.heapify(que)
    count = 0
    answer = 0
    while que and count <= n:
        cost, city = heapq.heappop(que)
        if visited[city] == 0:
            visited[city] = 1
            count += 1
            answer += cost
            for next_cities in nodes[city]:
                heapq.heappush(que, next_cities)
    # print(answer)
    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
