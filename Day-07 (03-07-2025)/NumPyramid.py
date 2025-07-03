spaces = 40
number = 1
for i in range(0,10):
    for j in range(0,spaces):
        print(' ',end='')
    for j in range(0,number):
        print(i, end='')
    print()
    spaces -= 1
    number += 2
