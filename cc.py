# Define functions for your app's functionality
def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Define the main function to run the app
def main():
    print("Welcome to Simple Calculator App!")
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter operation number (1-5): ")

        if choice == '5':
            print("Exiting...")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add_numbers(num1, num2))
        elif choice == '2':
            print("Result:", subtract_numbers(num1, num2))
        elif choice == '3':
            print("Result:", multiply_numbers(num1, num2))
        elif choice == '4':
            print("Result:", divide_numbers(num1, num2))
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the application
if __name__ == "__main__":
    main()
