from calculator import add, subtract, multiply, divide
from advanced import sqrt, power, percentage

def print_menu():
    print("\nSimple Team Calculator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Sqrt")
    print("6) Power")
    print("7) Percentage")
    print("0) Exit")

def get_number(prompt):
    return float(input(prompt))

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "0":
            break
        try:
            if choice == "1":
                a = get_number("a: "); b = get_number("b: ")
                print("Result:", add(a,b))
            elif choice == "2":
                a = get_number("a: "); b = get_number("b: ")
                print("Result:", subtract(a,b))
            elif choice == "3":
                a = get_number("a: "); b = get_number("b: ")
                print("Result:", multiply(a,b))
            elif choice == "4":
                a = get_number("a: "); b = get_number("b: ")
                print("Result:", divide(a,b))
            elif choice == "5":
                a = get_number("value: ")
                print("Result:", sqrt(a))
            elif choice == "6":
                a = get_number("base: "); b = get_number("exponent: ")
                print("Result:", power(a,b))
            elif choice == "7":
                part = get_number("part: "); whole = get_number("whole: ")
                print("Result (%):", percentage(part, whole))
            else:
                print("Invalid option")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()