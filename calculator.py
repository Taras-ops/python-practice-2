num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sign = input("Enter sign: ")

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)
else:
    print('Sign is not valid')