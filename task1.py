def get_valid_number():
    while True:
        try:
            num = int(input("Enter a number between 3 and 9: "))
            if 3 <= num <= 9:
                return num
            else:
                print("Invalid input. Please enter a number between 3 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 3 and 9.")
num = get_valid_number()
print("Valid number entered: ", num)