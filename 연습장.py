a, b, c = map(int, input().split())
def main():
    if b%2 == 0:
        print(involution(a, b)%c)
    else:
        print(involution_odd(a, b)%c)

def involution(a, b) -> int:
    
    if b == 1:
        return a
    else:
        tmp = involution(a, b//2)%c
        return (tmp * tmp)%c

def involution_odd(a, b) -> int:
    if b == 1:
        return a
    else:
        tmp = involution(a, (b-1)//2)%c
        return (tmp * tmp * a)%c

if __name__ == '__main__':
    main()