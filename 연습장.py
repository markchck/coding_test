def solution(targets):
    # end를 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    s, e = 0
    answer = 0
    for target in targets:
        if (target[0] >= e):
            answer += 1
            e = target[1]
        else:
            continue
    return answer


solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]])
