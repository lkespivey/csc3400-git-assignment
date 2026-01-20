import calculator

def main():
    print("What function would you like to perform on these numbers? Input up to two.")

    f = input("add|subtract|multiply|divide|sqrt|power")

    if f in ["add", "subtract", "multiply", "divide", "power"]:
        x = float(input("first:"))
        y = float(input("second:"))

    elif f == "add":
        print(calculator.add(x, y))
    
    elif f == "subtract":
        print(calculator.subtract(x, y))

    elif f == "multiply":
        print(calculator.multiply(x, y))
    
    elif f == "divide":
        print(calculator.divide(x, y))
    
    elif f == "power":
        print(calculator.power(x, y))

    elif f == "sqrt":
        p = float(input("number:"))
        print(calculator.power(p))
    
    if __name__ == "__main__":
        main()