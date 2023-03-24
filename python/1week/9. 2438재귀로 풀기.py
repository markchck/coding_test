n = int(input())

def starprint(i):
    if i==1:
        print('*')
    else:
        starprint(i-1)
        print('*'*i)

starprint(n)


