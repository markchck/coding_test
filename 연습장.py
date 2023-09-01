def solution(arr):
    N = len(arr)
    first = arr[0][0]
    red, blue = 0, 0
    flag = True
    for r in range(N):
        for c in range(N):
            if arr[r][c] != first:
                flag = False
                break

    if flag == True:
        if first == 0:
            red += 1
        else:
            blue += 1
    else:  # 자르기 들어가야함.
        newN = N//2
        # arr1, arr2, arr3, arr4 = [], [], [], []
        arr1 = [[0] * newN for _ in range(newN)]
        arr2 = [[0] * newN for _ in range(newN)]
        arr3 = [[0] * newN for _ in range(newN)]
        arr4 = [[0] * newN for _ in range(newN)]

        for r in range(N):
            for c in range(N):
                if 0 <= r < newN and 0 <= c < newN:
                    arr1[r % newN][c % newN] = (arr[r][c])
                elif 0 <= r < newN and newN <= c < N:
                    arr2[r % newN][c % newN] = (arr[r][c])
                elif newN <= r < N and 0 <= c < newN:
                    arr3[r % newN][c % newN] = (arr[r][c])
                else:
                    arr4[r % newN][c % newN] = (arr[r][c])
        solution(arr1)
        solution(arr2)
        solution(arr3)
        solution(arr4)
    return [red, blue]


solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
