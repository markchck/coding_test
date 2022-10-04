import sys

def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    lp = 0
    rp = n-1
    lastdata = [2000001048,lp,rp]

    while lp < rp:
        summed = arr[lp]+arr[rp]
        if summed == 0:
            print(arr[lp], arr[rp])
            return
        if abs(summed) < lastdata[0]:
            lastdata[0], lastdata[1], lastdata[2] = abs(summed), lp, rp
        if summed < 0:
            lp += 1
        else:
            rp -= 1

    print(arr[lastdata[1]], arr[lastdata[2]])
        

main()