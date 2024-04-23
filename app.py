from calc_func import do_addition, do_subtraction
from multiply import do_multiplication
from area import calculate_area_rectangle

def main():
    print("Welcome to the calculator app")
    print("""
        \n Select the function from the given options:
        1. Add
        2. Subtract
        3. Multiplication
        4. Area
    """)

    user_input = input("Select the function")

    a = int(input("Value of A"))
    b = int(input("Value of B"))

    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_subtraction(a,b)
    elif user_input == '3':
        result = do_multiplication(a,b)
    elif user_input == '4':
        result = calculate_area_rectangle(a,b)

    print(result)

if __name__ == '__main__':
    main()