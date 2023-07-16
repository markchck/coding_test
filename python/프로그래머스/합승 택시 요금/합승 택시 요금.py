# 다익스트라가 대체 뭐길래 이렇게 복잡한 문제를 해결할 수 있단건지 함 보자
import heapq
import sys


def dijkstra(s, e):
    global length, graph
    # 모든 노드의 cost를 최대로 설정
    # max값을 기본으로 넣었기 때문에 외딴 섬처럼 그래프가 끊긴 노드들은 항상 최대값이 들어가게 되고 따라서 dfs나 bfs로 그래프가 연결된 건지 확인하는 식의 로직이 필요가 없는 것
    visit = [sys.maxsize] * (length + 1)
    visit[s] = 0  # 시작점은 cost가 0이니까
    pq = [[0, s]]  # cost, node 순서로 힙에 넣을거임
    heapq.heapify(pq)

    while pq:
        cost, node = heapq.heappop(pq)
        # 지금 보는 도시보다 더 빨리가는 방법을 이미 기록해서 알고 있으면 더 볼 필요 없이 패스해야지.
        if cost > visit[node]:
            continue
        for i in graph[node]:  # 지금 보고 있는 도시와 연결된 도시들을 전부 가봐야함
            new_node, new_cost = i[0], i[1]
            new_cost += cost  # 비용은 누적해서 더해주고

            if new_cost < visit[new_node]:  # 지금 기록해놓은 것보다 더 짧은 루트가 생기면 갈아끼워주고
                visit[new_node] = new_cost
                # 현재 노드(new_node)가 더 짧은 루트이기 때문에 현재 노드와 연결된 애들을 보면 됨.
                heapq.heappush(pq, [new_cost, new_node])
    return visit[e]


def solution(n, s, a, b, fares):
    global length, graph
    answer = sys.maxsize
    length = n
    graph = [[] for _ in range(n+1)]
    # [[], [(6, 25), (3, 41), (4, 10), (5, 24)], [(3, 22), (4, 66)], [(2, 22), (1, 41), (5, 24)], [(2, 66), (1, 10), (6, 50)], [(3, 24), (1, 24), (6, 2)], [(1, 25), (4, 50), (5, 2)]]

    # 왜 graph에 관계 설정을 한 번 더 하냐?(이미 fares에 관계가 들어있는거 아니냐?)
    # fares에 관계설정이 이미 되어있긴한데 fares에 나온대로 [1 4 10]이면 [4 1 10]도 된다는 걸 컴퓨터는 모르잖아. (인간은 문자로 쌍방향이라는 걸 알 수 있지만)
    # 그리고 1번 루트가 어디 어디랑 연결 되어있는지 fares만 봐서는 바로 안나온다.
    # graph로 재가공을 해줘야 6,3,4,5번이랑 연결되어있다는 것을 바로 알지.
    # 백준도 똑같이 관계 설정 한 번 더 해준다.
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])

    for i in range(1, n+1):  # for문을 돌며 모든 노드를 본다.
        # 다익스트라 함수 구현 부분은 막상 국밥 같이 반복되는 느낌이고 사실 이 부분이 핵심이다.
        # 어떻게 각자 갈 수도 있고 합승할 수도 있는 상황에서 최적의 비용을 찾을까?
        # 일단 출발점에서 i노드까지 최소비용으로 가고 거기서 a집까지 가는 최소비용에 + b집까지 가는 최소 비용을 더한 값을 구한 뒤
        # i까지 가는 비용으로 지금 알고있는 answer보다 더 작으면 갈아 끼우고 더 크면 기존 answer를 쓴다.
        # 재귀 + 다익스트라+ BFS 짬뽕
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer


solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
         5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
