import os
def main():
    print("Application here")
def encrypt(a):
    t=[]
    for b in a:
        t.append(str(ord(b)))
    return t
def decrypt(a):
    t=""
    for x in a:
        t=t+chr(x)
    return t
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
    t=encrypt(cu)
    c=""
    for d in t:
        c=c+d       
    c=c+"\n"       
    for x in fl:
        if x==c:#check id and pw
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
    t=encrypt(cu)
    c=""
    for d in t:
        c=c+d       
    c=c+"\n"
    for x in f:#in caSE user account exisTs
        if x==c:
            print("YOUR ACCOUNT ALREADY EXISTS!")
            exisTs=True
            break
    if exisTs==False:
        f=open("data.txt","at")
        f.writelines(encrypt(cu))
        f.write("\n")
        f.close()
        print("Account successfuly created.")
else:
    print("Wrong Choice!")  