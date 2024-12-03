card_number = list(input("Please Enter your Credit card number: ").strip())
check_digit = card_number.pop()
card_number.reverse()

processed_digits =[]
total = 0

for index ,digits in enumerate(card_number):
    if index % 2 == 0:
        double_digit = int(digits)*2
        if double_digit > 9:
            double_digit = double_digit -9
        processed_digits.append(double_digit)
    else:
       processed_digits.append(int(digits))
    
    total = sum(processed_digits)

if total % 10 == 0:
    print("valid")
else: 
    print("invalid")