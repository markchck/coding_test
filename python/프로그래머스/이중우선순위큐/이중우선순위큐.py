import heapq

big = []
small = []


def solution(operations):
    for operation in operations:
        action, value = operation.split(" ")
        value = int(value)
        if action == 'I':
            heapq.heappush(big, (-value, value))
            heapq.heappush(small, value)
        else:  # action은 D이고
            if value == -1:
                if small:
                    smallest = heapq.heappop(small)
                    big.remove((-smallest, smallest))
            else:  # value가 1인 경우 (최대를 Pop해야하는데..)
                if big:
                    biggest = heapq.heappop(big)[1]
                    small.remove(biggest)
    # result = []
    # # big, small 동기화
    # for s in small:
    #     for b in big:
    #         bb = b[1]
    #         if s == bb:
    #             result.append(s)

    if not small:
        return ([0, 0])
    else:
        return ([max(small), min(small)])


solution(["I -45", "I 653", "D 1", "I -642",
         "I 45", "I 97", "D 1", "D -1", "I 333"])
