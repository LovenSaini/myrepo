import os
def main():
    f=open("data.txt")
    for x in f:
        print(x)
print("HELLO USER!")
print("Press 1 for Sign In OR press 2 for SIGN UP(New User)")
ch=int(input())
call=False
if ch==1:#EXISTING USER SIGN IN
    print("Enter Username:",end=" ")
    user=input()
    print("Enter Password:",end=" ")
    pw=input()
    f=open("data.txt","rt")
    cu=user+" "+pw
    for x in f:
        if x==cu:
            print("ACCESS GRANTED")
            main()
            call=True
        else:
            print(x)
        if call==False:
            print("WRONG CREDENTIALS")
    f.close()
elif ch==2: #NEW USER SIGN UP
    f=open("data.txt","rt")
    print("Enter Username to sign up:",end=" ")
    user=input()
    print("Enter Password:",end=" ")
    pw=input()
    cu=user+" "+pw
    for x in f:#in caSE user account exisTs
        if x==cu:
            print("YOUR ACCOUNT ALREADY EXISTS!")
    f=open("data.txt","at")
    f.write('\n')
    f.write(cu)
    f.close()
else:
    print("Wrong Choice!")