'''
if <условие прерывания>:
    break

if <условие пропуска>:
    continue
'''
for symbol in 'Hello world':
    if symbol == 'o':
        break
    print(symbol)

for symbol in 'Hello world':
    if symbol == 'o':
        continue
    print(symbol)