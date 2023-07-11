def solution(sequence, k):
    sum, left, right = 0, 0, 0
    answer = []
    while True:
        if sum < k:  # 부분합이 k가 되기엔 부족하니까 right를 오른쪽으로 옮겨서 부분합을 늘려줘야함.
            if right > len(sequence)-1:  # right가 늘어날 수 있는 최대는 배열의 마지막 인덱스까지임
                break
            # 정상적으로 right가 늘어도 되는 상황
            sum += sequence[right]
            right += 1
            continue

        if sum == k:
            answer.append([left, right-1])
            # sum==k를 찾고 끝난게 아니라 다른 쌍을 또 찾아야하기 때문에 right를 늘려줘야함.
            if right > len(sequence)-1:
                break
            sum += sequence[right]
            right += 1
            continue

        if sum > k:  # 부분합이 너무 길어져서 k보다 커진 상황. 부분합을 줄여야하기 때문에 left를 오른쪽으로 이동해야함.
            if left > right:  # left는 right를 넘어설 수는 없다.
                break
            sum -= sequence[left]
            left += 1
            continue

    answer.sort(key=lambda x: (x[1]-x[0]))
    return answer[0]


solution([1, 1, 1, 2, 3, 4, 5], 5)
