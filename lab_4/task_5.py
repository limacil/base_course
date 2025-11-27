from scipy.constants import pi

print('1 - круг; 2 - прямоугольник; 3 - треугольник')
v = int(input('выбор:'))

if v == 1:
    r = int(input('радиус:'))

if v == 2:
    st_1 = int(input('сторона_1:'))
    st_2 = int(input('сторона_2:'))

if v == 3:
    h = int(input('высота:'))
    st_h = int(input('сторона, прилегающая к высоте:'))


def krug_pl (r):
    s_kr = 2 * pi * r
    print(f'площадь круга: {s_kr}')
    return s_kr


def priam_pl (st_1, st_2):
    
    s_pr = st_1 * st_2
    print(s_pr)
    return s_pr


def tre_pl (h, st_h):
    s_tr = h * st_h / 2
    print(s_tr)
    return s_tr


if v == 1:
    krug_pl (r)

if v == 2:
    priam_pl (st_1, st_2)

if v == 3:
    tre_pl (h, st_h)