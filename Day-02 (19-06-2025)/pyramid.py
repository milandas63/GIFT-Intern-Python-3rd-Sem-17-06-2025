spaces = 40
stars = 1

for i in range(0,10):
    for j in range(0,spaces):
        print(' ',end='')
    for j in range(0,stars):
        print('*',end='')
    print()
    spaces = spaces-1
    stars = stars + 2
