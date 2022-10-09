import os
def main():
    f=open("data.txt")
    for x in f:
        print(x)
    f.close()
print("HELLO USER!")
print("Press 1 for Sign In OR press 2 for SIGN UP(New User):",end=" ")
ch=int(input())
call=False
if ch==1:#EXISTING USER SIGN IN
    print("Enter Username:",end=" ")
    user=input()
    print("Enter Password:",end=" ")
    pw=input()
    f=open("data.txt","rt")
    fl=f.readlines()
    cu="id:"+user+" "+"pw:"+pw+"\n"              
    for x in fl:
        if x==cu:#check id and pw
            print("ACCESS GRANTED")
            main()
            call=True
            break
        
    if call==False:
         print("WRONG CREDENTIALS")
    f.close()
elif ch==2: #NEW USER SIGN UP
    exisTs=False
    f=open("data.txt","rt")
    print("Enter Username to sign up:",end=" ")
    user=input()
    print("Enter Password:",end=" ")
    pw=input()
    cu="id:"+user+" "+"pw:"+pw+"\n"
    for x in f:#in caSE user account exisTs
        if x==cu:
            print("YOUR ACCOUNT ALREADY EXISTS!")
            exisTs=True
            break
    if exisTs==False:
        f=open("data.txt","at")
        f.write(cu)
        f.close()
        print("Account successfuly created.")
else:
    print("Wrong Choice!")