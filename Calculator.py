num1, type, num2= input("Enter Number").split()

if type == "+":
    sum = int(num1)+int(num2)
    print(f"{num1}+{num2}={sum}")
if type == "-":
    sub= int(num1)-int(num2)
    print(f"{num1}-{num2}={sub}")
if type == "x":
    mul = int(num1)*int(num2)
    print(f"{num1}x{num2}={mul}")
#alt+0247
if type == "÷" or type == "/":
    div = int(num1)/int(num2)
    print(f"{num1}÷{num2}={div}")