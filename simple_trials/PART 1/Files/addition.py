"""This program tries to make sure the user enters the right input for addition"""
print("Enter 'q' to quit.")
print("Enter two numbers for addition.")



try:
    while True:
        num_one = input("\nEnter the first number: ")
        if num_one == 'q':
            break
        num_two = input("Enter the second number: ")
        if num_two == 'q':
            break
        result = int(num_one) + int(num_two)
        print(f"The addition of {num_one} and {num_two} is", result)
except ValueError:
    print("Enter a valid number.")
else:
    print(result)