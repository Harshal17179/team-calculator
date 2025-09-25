import math

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(x)

def power(base, exponent):
    return base ** exponent

def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole cannot be zero for percentage calculation")
    return (part / whole) * 100

# simple self-test
if __name__ == "__main__":
    print("sqrt(16) =", sqrt(16))
    print("2^8 =", power(2,8))
    print("percentage(25,200) =", percentage(25,200))