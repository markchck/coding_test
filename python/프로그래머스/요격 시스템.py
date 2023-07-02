# 실수에서도 요격
# s,e에서는 용격 불가
# 가장 길게 분포된놈 먼저 뽑아서 count +1해주고
# 배열에서 분포된 놈 범위 안에 들어오는 놈들은 전부 빼 (방금 쏜 미사일 한방으로 해결 가능하니까)
# 다음 가장 길게 분포된놈 뽑아서 또 count +1...(반복))
# 배열에 아무것도 남은게 없으면 리턴


targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]


def sort_by_second_elemnet(arr):
    return arr[1]


def solution(targets):
    targets.sort(key=sort_by_second_elemnet)

    s = e = 0
    answer = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
    return answer


def solution(targets):
    targets.sort()
    answer = 1
    e = targets[0]

    for target in targets[1:]:
        if (target[0] >= e):
            answer += 1
            e = target
        else:
            if (target[1] < e):
                # 왜 end를 줄여야하는지 생각하기가 엄청 어려울듯? (최대한 End를 넓게 잡는게 유리한거 아닌가?)
                # [1,4], [2,3]이 있다고 생각하면 end를 4에서 3으로 줄여야 [1,4]랑 [2,3] 둘 다 요격할 수 있다.
                e = target[1]

# def solution(targets):
#     targets.sort(key=lambda x: x[1])
#     s = e = 0
#     answer = 0
#     for target in targets:
#         if target[0] >= e:
#             answer += 1
#             e = target[1]
#     return answer


# def sort_by_second_elemnet(arr):
#     return arr[1]
# def solution(targets):
#     targets.sort(key=sort_by_second_elemnet)

#     s = e = 0
#     answer = 0
#     for target in targets:
#         if target[0] >= e:
#             answer += 1
#             e = target[1]
#     return answer


solution(targets)
