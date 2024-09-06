# import bcrypt
# password = b'Password'
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password, salt)
# print("Salt :",salt)
# print("Hashed",hashed)


# Here input takes form the user
import bcrypt
password = input("Enter your password: ").encode('utf-8')  # Encode the password as a byte string
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
print("Salt    :", salt)
print("Hashed  :", hashed)

# import hashlib

# def hash_password(password, salt):
#     password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
#     return password_hash

# def verify_password(stored_password, provided_password, salt):
#     password_hash = hashlib.sha256((provided_password + salt).encode('utf-8')).hexdigest()
#     return password_hash == stored_password

# user_password = "Your Passowrd"
# provided_salt = "Your Salt"  # Replace with your specific salt key
# hashed_password = hash_password(user_password, provided_salt)
# print("Hashed Password:", hashed_password)
# provided_password = "Provided Passowrd"
# password_matched = verify_password(hashed_password, provided_password, provided_salt)
# print("Password Matched:", password_matched)