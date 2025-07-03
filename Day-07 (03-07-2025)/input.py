##############################
# INPUT and OUTPUT operation #
##############################
import os

more = True
handle = open("personal-data.txt", "a")

while(more):
    os.system("cls")
    print("PERSONAL DATA")
    print("-------------")
    slno =   input("Serial No.:        ")
    name =   input("What is your name: ")
    father = input("Father's name:     ")
    gender = input("Gender [M/F]:      ")
    email =  input("Email-id:          ")
    phone =  input("Mobile No.:        ")
    
    buffer = f"{slno},{name},{father},{gender},{email},{phone}\r\n"
    #buffer = f"{slno}\r\n{name}\r\n{father}\r\n{gender}\r\n{email}\r\n{phone}\r\n"
    handle.write(buffer)
    
    print()
    more = input("More [Y/N]: ").upper().startswith("Y")

handle.close()
    
    

