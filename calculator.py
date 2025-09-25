def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# simple self-test
if __name__ == "__main__":
    print("2 + 3 =", add(2,3))
    print("5 - 1 =", subtract(5,1))
    print("4 * 6 =", multiply(4,6))
    print("8 / 2 =", divide(8,2))