from calc_func import do_addition, do_subtraction

def main():
    print("Welcome to the calculator app")
    print("""
        \n Select the function from the given options:
        1. Add
        2. Subtract
    """)

    user_input = input("Select the function")

    a = int(input("Value of A"))
    b = int(input("Value of B"))

    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_subtraction(a,b)

    print(result)

if __name__ == '__main__':
    main()