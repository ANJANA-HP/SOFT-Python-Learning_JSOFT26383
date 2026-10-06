num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))    

if operator == "+":
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", result)   
elif operator == "-":
    result = num1 - num2
    print("The difference of", num1, "and", num2, "is:", result)    
elif operator == "*":
    result = num1 * num2
    print("The product of", num1, "and", num2, "is:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("The division of", num1, "by", num2, "is:", result)
else:
        print("Error: Invalid operator.")