def do_division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "Divisible by zero not accepted"