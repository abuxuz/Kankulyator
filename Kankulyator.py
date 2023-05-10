# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Qo'shish")
print("2.Ayirish")
print("3.Ko'paytirish")
print("4.Ayirish")

while True:
    # take input from the user
    choice = input("Birini tanlang: (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Birinchi raqamni kiriting: "))
            num2 = float(input("Keyingi raqamni kiriting: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Keyini hisobni kiritasizmi? (Ha/Yoq): ")
        if next_calculation == "Yoq":
            break
    else:
        print("Canculator")

