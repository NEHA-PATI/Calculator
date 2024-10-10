print("                                                                                                                        ")
print("                                                         SIMPLE BASIC CALCULATOR                                        ")
print("                                                                                                                        ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("------------------------------------------------------------------------------------------------------------------------")
operator = input("Enter an operator for calculation(+ - * / **): ")
print("------------------------------------------------------------------------------------------------------------------------")
#Operations performed by each operator
if operator=="+":
    result=num1 + num2
    print("Result:", round(result, 3))
    print("--------------------------------------------------------------------------------------------------------------------")
elif operator=="-":
    result=num1-num2
    print("Result:", round(result, 3))
    print("--------------------------------------------------------------------------------------------------------------------")
elif operator =="*":
    result=num1* num2
    print("Result:", round(result, 3))
    print("--------------------------------------------------------------------------------------------------------------------")
elif operator=="/":
    result=num1/num2
    print("Result:", round(result, 3))
    print("--------------------------------------------------------------------------------------------------------------------")
elif operator=="**":
    result=num1**num2
    print("Result:", round(result, 3))
    print("--------------------------------------------------------------------------------------------------------------------")
else:
    print("Enter a valid operator to perform the operation")
