
# if elif statement 
# number=int(input("enter the correct number:"))
# if number%3 == 0 and number%10 ==0 and number%7 ==0:
#     print ("fitbit2")
# elif number%3 == 0:
#     print ("fit")
# elif number%10 == 0:
#     print("bit")   
# elif number%7 == 0:
#     print ("2")
# else:
#     print ("Ok")

#nested-if statement
age=int(input("enter the age:"))
gender =input("enter male/female:")
messages={
    ("male", True): "below 30 male",
    ("male", False): "",  
    ("female", False): "above 30 female",
    ("female", True): ""  
}

message = messages.get((gender, age < 30), "Invalid input")
print(messages)
