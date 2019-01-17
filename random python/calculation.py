# Program make a simple calculator that can add, subtract, multiply, divide, exponent, floor, and modulus using functions

# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

# This one is exponents
def exponent(x, y):
    return x ** y

# Floor Division
def fldiv(x, y):
    return x // y

# Modulus
def modulus(x, y):
    return x % y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5. Exponent")
print("6. Floor Division")
print("7. Modulus Equation")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
    print(num1,"^",num2,"=", exponent(num1,num2))
elif choice == '6':
    print(num1,"//",num2,"=", fldiv(num1,num2))
elif choice == '7':
    print(num1,"%",num2,"=", modulus(num1,num2))
else:
   print("Invalid input")
print("press enter to exit.")
exit = input()
