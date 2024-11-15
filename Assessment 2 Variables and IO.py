num1 = float(input("Enter the first number: "))
num2 = float (input("Enter the second number: ")) 
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
if num2 != 0:
divid = num1 / num2
else:
divid = "cannot divide by zero" 
print(num1, "sum", num2, "is", add)
print(num1, "difference", num2, "is", subtract)
print(num1, "product", num2, "is", multiply)
print(num1, "quotient", num2, "is", divid)
