"""
                        a         
                       aba        
                      abcba       
                     abcdcba      
                    abcdedcba     
                   abcdefedcba    
                  abcdefgfedcba   
                 abcdefghgfedcba  
                abcdefghihgfedcba 
               abcdefghijihgfedcba
"""
spaces = 40

for i in range(0,11):
    for j in range(0, spaces):
        print(' ', end='')
    for j in range(0, i):
        print(chr(j+97), end='')
    for j in range(i, -1, -1):
        print(chr(j+97), end='')
    print()
    spaces -= 1
