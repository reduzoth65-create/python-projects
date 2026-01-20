try:
    num1, num2=eval(input("Enter 2 numbers, seprated by comma:"))
    result=num1/num2
    print("Result is",result)

except ZeroDivisionError:
    print("Division by 0 is Error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")