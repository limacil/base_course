ch = int(input('Число: '))
st = str(ch)
b = ''
## b = str(b)
## a = 0
for i in range(len(st)):
    ## a = int(a)
    a = ch % 10
    ch = ch // 10
    a = str(a)
    b += str(a)
print(b)