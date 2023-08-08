# 크루스칼
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    def find_parent(parent, n):
        if parent[n] == n:
            return n
        else:
            parent[n] = find_parent(parent, parent[n])
            return parent[n]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    for node_a, node_b, cost in costs:
        a = find_parent(parent, node_a)
        b = find_parent(parent, node_b)
        # 싸이클 여부 확인 (a와 b의 부모가 달라야함. 같으면 싸이클 생긴 것)
        if a != b:
            # 싸이클이 없기 때문에 a, b를 연결
            union_parent(parent, node_a, node_b)
            answer += cost
    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
