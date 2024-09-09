import random                           #we imported random module 
what = input("what is this pass for:")  #take input from the user 
pwd_len=int(input("Enter the length of the password:"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+.,/\[]{}_-='|"
pwd="".join(random.sample(s,pwd_len))
print('your pass:',pwd)
with open('password.txt','a') as f:
    data=what+'\n'+pwd+'\n\n'
    f.write(data)
    f.close


