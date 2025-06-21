spaces = 40
stars = 1
buf = ' '

for i in range(0,10):
    for j in range(0,spaces):
        print(' ',end='')
    for j in range(0,stars):
        if j==0 or j==stars-1 or i==9:
            buf = '*'
        else:
            buf = ' '
        print(buf,end='')
    print()
    spaces = spaces - 1;
    stars = stars + 2;
