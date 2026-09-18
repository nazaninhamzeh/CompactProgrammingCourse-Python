input_num = int(input("Input the number for factorial calculation : "))

if input_num < 0 :
    print("Wrong input - Factorial is not defined for negative numbers.")
else : 
    result = 1

    for i in range(1, input_num+1) :
        result *= i
    
    print(f"{input_num}! = {result}")