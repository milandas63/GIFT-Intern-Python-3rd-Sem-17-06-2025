# text = 'This text contains lots of vowels'
text = input('Enter some text: ')
vowels = 'AEIOUaeiou'
count = 0

for i in text:
    for j in vowels:
        if i==j:
            count += 1
            break
print('Total vowels =',count)
