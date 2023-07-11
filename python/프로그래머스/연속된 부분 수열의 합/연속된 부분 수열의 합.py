def solution(sequence, k):
    answer = []
    li = list(map(int, sequence))
    k = int(k)
    length = len(li)
    start_idx = 0
    end_idx = 0
    li_sum = 0

    while True:
        if li_sum < k:
            if end_idx >= length:
                break
            li_sum += li[end_idx]
            end_idx += 1

        elif li_sum > k:
            # li_sum이 목표한 k 보다 크면 왼쪽을 줄여서 k와 맞춰야하겠지?
            # 그런데 start_idx가 (왼쪽이) 이미 배열의 끝이라면 왼쪽을 더 줄일 수가 없다.
            # startidx나 Endidx 둘 다 배열의 길이를 넘을 수는 없는거니까
            # 그래서 break를 해준다.
            if start_idx >= length - 1:
                break
            li_sum -= li[start_idx]
            start_idx += 1

        elif li_sum == k:
            answer.append([start_idx, end_idx - 1])
            if end_idx >= length:
                break
            li_sum += li[end_idx]
            end_idx += 1

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]


solution([3], 3)
