
def calculator():
     number1 = input("Enter number 1:")
     number2 = input("Enter number 2:")
     operation = input("Enter operation (+, *, /, -): + ")
     # operation=['+','-','*','/']
     if operation == "+":
      result = int(number1) + int(number2)
     elif operation == "-":
      result = int(number1) - int(number2)
     elif operation == "*":
      result = int(number1) * int(number2)
     elif operation == "/":
      result = int(number1) / int(number2)
     else:
      print("Enter a valid operation.")
     print(result)


