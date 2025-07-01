l = ['god','good','better','excellent','nobel']
n = 3463
p = 3
try:
    print('Start of block')
    print(l[4])
    print(n/p)
    raise ArithmeticError()
except OSError:
    print('OS Error')
except KeyError:
    print('Key Error')
except ZeroDivisionError:
    print('Zero Division Error')
except ArithmeticError:
    print('Arithmetic Error')
except IndexError:
    print('This is index error')
else:
    print('Error doesn\'t match with any except')
finally:
    print('This block is executed by all situations')
