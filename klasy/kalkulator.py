from liczby_zespolone import Complex

while True:
    print("Enter complex numbers values in form [re1], [im1], [re2], [im2]")
    equation = input()

    print("Input operation (+, -, *)")
    operation = input()

    try:
        equation = equation.replace(" ", "")
        table = equation.split(",")

        num1 = Complex(int(table[0]), int(table[1]))
        num2 = Complex(int(table[2]), int(table[3]))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2

        print(str(num1) + " " + operation + " " + str(num2) + " = " + str(result))

    except:
        print("Error \n")
