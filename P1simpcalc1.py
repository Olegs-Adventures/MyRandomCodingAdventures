""""
My first working program.
Looks simple, was simple, still bad

"""

num1 = float(input("First number: "))
print("First number is: ", num1)
operator1 = input("Input operator: ")
print("Operator is: ", operator1)
num2 = float(input("Second number: "))
print("Second number is: ", num2)

if operator1 == "-":
    result = num1 - num2
    print(result)
elif operator1 == "+":
    result = num1 + num2
    print(result)
elif operator1 == "/":
    result = num1 / num2
    print(result)
elif operator1 == "*":
    result = num1 * num2
    print(result)
else:
    print("Invalid")
