ch = int(input('Число: '))
i = 2
print(f"Простые множетели числа {ch}:", end = " ")

while i <= ch:
    if ch % i == 0:
        print(i, end = " ")
        ch //= i
    else:
        i += 1

