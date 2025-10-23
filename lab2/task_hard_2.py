a, b, c = int(input("Первая сторона: ")), int(input("Вотрая сторона: ")), int(input("Третья сторона: "))

if a + b > c and a + c > b and b + c > a:
    print('Такой треугольник существует')
    
    if a == b or a == c or b == c:
        if a == b == c:
            print('Он равносторонний')
        else:
            print('Он равнобедренный')
    if a < b < c or b < c < a or c < a < b:
        print('Он разносторонний')
else: 
    print('Такого треугольника не существует(')