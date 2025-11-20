def my_func(a, b):
    x = 3 * a - b
    return x


# tmp = my_func()


def my_func(a = 1, b = 0):
    x = 3 * a - b
    return x


tmp = my_func()
print(tmp)
print(my_func(3,4))

print(my_func(3))

print(my_func(b = 3))

print(my_func(b = 3, a = 9))


def my_func(*args):
    x = 3 * (args[0] - args[1]) / len(args)
    return x

print(my_func(3, 4))

print(my_func(3, 4, 8))

def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x


print(my_func(obj_1 = 3, obj_2 = 4))
print(my_func(obj_1 = 3, obj_2 = 4, obj_3 = 8))


def final_func(a: float, b: int = 1, c = 4, *arg, **kw):
    print(f'Hello world {a} + {b} + {c} - {arg} / {kw} ')
    

final_func(1)
final_func(1, 4)
final_func(1, 4, 6)
final_func(1, 4, 6, 'fhfg', 4, 8)
final_func(1, f = 5, h = 'Good')
final_func('ggwp')