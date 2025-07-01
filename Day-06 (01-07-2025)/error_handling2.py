class AgeError(Exception):
    def __init__(self):
        print('Age error')

class AgeCeilingError(AgeError):
    def __init__(self):
        print('Age is not in range')

class TooOldAgeError(AgeCeilingError):
    def __init__(self):
        print('Too old age')

class TooYoungAgeError(AgeCeilingError):
    def __init__(self):
        print('Too old age')

class InvalidDataError(AgeError):
    def __init__(self):
        print('Invalid age')

class NegativeAgeError(InvalidDataError):
    def __init__(self):
        print('Negative age')

class ZeroAgeError(InvalidDataError):
    def __init__(self):
        print('Zero age')

ages = [22,34,91,67,83,41,11,-25,66,35,0,51,77,102,18,90,17,91]

for age in ages:
    try:
        if age<0:
            raise NegativeAgeError
        elif age==0:
            raise ZeroAgeError
        elif age<18:
            raise TooYoungAgeError
        elif age>90:
            raise TooOldAgeError
        print(age, 'is valid age')
    except TooOldAgeError:
        print(age, 'is greater than 90')
    except TooYoungAgeError:
        print(age, 'is less than 18')
    except NegativeAgeError:
        print(age, 'is minus')
    except ZeroAgeError:
        print(age, 'is zero')



