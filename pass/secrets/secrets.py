# import secrets 
# pass_length=12
# print(secrets.token_bytes(pass_length))


import secrets
password_length = 13
print(secrets.token_urlsafe(password_length))