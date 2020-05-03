num1 = float(input("Enter a number:"))
op = input("Enter the operator:")
num2 = float(input("Enter Second number:"))

if op == "+":
    print("Sum is " + str((num1 + num2)))
elif op == "-":
    print("Difference is " + str((num1 - num2)))
elif op == "*":
    print("Multiple is " + str((num1 * num2)))
elif op == "/":
    print("Divisible by " + str((num1 / num2)))
elif op == "%":
    print("Remainder is " + str((num1 % num2)))
else:
    print("Invalid operator:")
