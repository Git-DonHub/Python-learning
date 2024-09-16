num1 = int(input("Enter first number: "))
action = input('Choose a mathematical operation:\n+\n-,\n*\n/')
num2 = int(input("Enter second number: "))
if action == '+':
    print(num1,'+',num2,'=',num1+num2)
elif action == '-':
    print(num1,'-',num2,'=',num1-num2)
elif action == '*':
    print(num1,'*',num2,'=',num1*num2)
elif action == '/':
    print(num1,'/',num2,'=',num1/num2)
else:
    print("Invalid input")
