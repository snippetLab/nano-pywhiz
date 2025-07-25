print("+ - Addition");
print("- - Substraction");
print("* - Multiplication");
print("/ - Division");
print("% - Modulas");

option = str(input("Choose Operation : "));

if (option in ["+", "-", "*", "/", "%"]) :
    numOne = int(input("Number One : "))
    numTwo = int(input("Number Two : "))
else :
    print("Invalid Operation")

if option == "+" :
    print("Addition : ", numOne + numTwo);

if option == "-" :
    print("Substraction : ", numOne - numTwo);

if option == "*" :
    print("Multiplication : ", numOne * numTwo);

if option == "/" :
    print("Divison : ", numOne / numTwo);

if option == "%" :
    print("Modulas : ", numOne % numTwo);