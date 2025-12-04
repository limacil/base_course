import time as tm

time = tm.time()
a = 0

def oracle(M, N):
    a = 0
    while a <= M:
        print(a)
        a += 1
        tm.sleep(1)


    def origin():
        nonlocal N
        global a
        while a <= N:
            print(a)
            a += 1
            tm.sleep(1)

        return a
    origin()

oracle(5, 6)

print(f'{tm.time() - time}, seconds')

