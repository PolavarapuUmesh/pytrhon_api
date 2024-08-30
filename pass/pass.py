import random

pass_gen=input("what is this pass for:")
pass_len=int(input("enter len of the pass:"))
s='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+={}[]|\:;"<>,.?/~`'
pwd=''.join(random.sample(s,pass_len))
print("random_pass:",pwd)

with open('password.txt','a') as f:
    data= pass_gen+ '\n'+pwd+'\n\n'
    f.write(data)
    f.close()


#Generate secret 
# import secrets
# password_length = 13
# print(secrets.token_urlsafe(password_length)






