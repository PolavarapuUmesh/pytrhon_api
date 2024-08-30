import bcrypt
password = b'GeekPassword'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
print("Salt :")
print(salt)
print("Hashed")
print(hashed)
