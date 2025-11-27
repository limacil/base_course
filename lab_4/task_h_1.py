a, n = int(input('a: ')), int(input('n: ')) 



def stepen (a,n):
    ch = a
    for i in range(n - 1):
        ch *= a
    print(ch)
    return ch


stepen(a, n)
    