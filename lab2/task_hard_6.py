k = int(input("Год нашей эры? 1 - да / 0 - нет:"))
den, mes, g = int(input("День: ")), int(input("Месяц: ")), int(input("Год: "))
if k == 1:
    ## a = 2000
    b = 776
    c = g + b
    d = 1 + abs(c // 4)
    e = c % 4 + 1
else:
    ## a = 480
    b = 776
    c = g - b
    d = 1 + abs(c//4)
    e = c % 4 + 1
if mes < 7:
    d -= 1
    e = 4

print (f'День: {den}, месяцx: {mes}, год: {d}.{e}')