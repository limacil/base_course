name = 'Rzhanov Arkadiy'

print('_'.join(name))
print(name.upper())
name = name.upper()
sym = [ord(sm) for sm in name]
print(sym)
print(f'наим:{min (sym)}, наиб: {max(sym)}')

name = name.lower()
print(name.lower())
sym = [ord(sm) for sm in name]
print(sym)
print(f'наим:{min (sym)}, наиб: {max(sym)}')