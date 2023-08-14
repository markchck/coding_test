# 힙으로 최대를 뽑으면서
# 완전탐색을 하고
# 뽑은놈의 양 옆을 disabled시키고, 이미 뽑았거나, disabled된 것은 재방문하지 않고
# max값을 설정하고 더 큰 숫자가 나오면 max를 갱신해 나간다.
# 루프를 다 돌고나서 max를 출력하면 될 듯?

def solution(sticker):
    length = len(sticker)
    answer = -9999999999999999
    if length <= 3:
        answer = max(sticker)
        print(answer)
        return answer

    for i in range(length):
        new_sticker = sticker[i:] + sticker[0:i]
        sum = 0
        available = [0] * (length)
        for idx, number in enumerate(new_sticker):
            if available[idx] == 0:
                if idx == 0:
                    available[idx] = 1
                    available[idx + 1] = 1
                    available[length-1] = 1
                    sum += number
                elif idx == (length-1):
                    available[idx] = 1
                    available[0] = 1
                    available[idx - 1] = 1
                    sum += number
                else:
                    available[idx] = 1
                    available[idx + 1] = 1
                    available[idx - 1] = 1
                    sum += number
            else:
                continue  # 방문한 인덱스인 경우
        answer = max(answer, sum)
    print(answer)
    return answer


solution( [1000, 10, 10, 2000, 30] )
