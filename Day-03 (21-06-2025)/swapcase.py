name = 'Narendra Damodar Das Modi'

for c in name:
    if c.isupper():
        c = c.lower()
    elif c.islower():
        c = c.upper()
    print(c,end='')

print()
print()

for c in name:
    asc = ord(c)
    if asc>=65 and asc<=90:
        asc = asc + 32
    elif asc>=97 and asc<=122:
        asc = asc - 32
    print(chr(asc), end='')


