from collections import deque


def solution(picks, minerals):
    answer = 9878676
    names = {"diamond": 0, "iron": 1, "stone": 2}
    table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    que = deque()
    que.append((picks, -1, 0, 0, 0))

    while que:
        # 남은 곡갱이, 현재곡갱이, 현재곡갱이 잔여 횟수, 현재광물, 현재까지 피로도
        rest_picks, cur_pick, cur_pick_life, idx, idx_cost = que.popleft()

        # 광물을 모두 캤거나, 곡괭이를 모두 사용했으면 answer와 비교하여 갱신
        if (idx >= len(minerals) or (rest_picks == [0, 0, 0] and cur_pick_life == 0)):
            answer = min(answer, idx_cost)
            continue

        # 현재까지의 피로도가 answer보다 크거나 같으면 pass
        if idx_cost >= answer:
            continue

        # 다이아는 0, 철은 1, 돌은 2
        mineralIdx = names[minerals[idx]]

        # 현재 사용중인 곡괭이를 더 사용할 수 있는 경우
        if cur_pick_life > 0:
            next_rest_picks = rest_picks[:]
            que.append((next_rest_picks, cur_pick, cur_pick_life-1,idx+1, idx_cost + table[cur_pick][mineralIdx]))
        else:
            # 새로운 곡괭이를 선택해야 하는 경우, 각 곡괭이에 대한 경우를 큐에 넣음
            for i, rest in enumerate(rest_picks):
                if rest == 0:
                    continue
                next_rest_picks = rest_picks[:]
                next_rest_picks[i] -= 1
                que.append((next_rest_picks, i, 4, idx + 1, idx_cost + table[i][mineralIdx]))
    return answer


solution([1, 1, 0], ["stone", "stone", "iron", "stone", "diamond",
         "diamond"])
