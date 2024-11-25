"""""part-1"""


# username = "aymn"
# password = 1234

# a = input("username :")
# b = input("password :")

# if username == a and password == b:
#     print("hogya login ")
# elif username != a and password != b: 
#     print("fail")

"""""part-2"""
 
username = "aymn"
password = 1234

a = input("username:")
b = int (input("password:"))

# while username != True or password != True:

if username == a and password == b:
    print("success")
elif username != a and password == b:
    print("username wrong")
elif username == a and password != b:
    print("password wrong")
elif username != a and password != b:
    print("failed")

