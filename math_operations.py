def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus by zero is not allowed")
    return a % b

def integer_division(a, b):
    if b == 0:
        raise ValueError("Integer division by zero is not allowed")
    return a // b
