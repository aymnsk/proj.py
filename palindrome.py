user = input("word:")

if user == user[::-1]:
    print("confirm")
else:
    print("not palindrome")