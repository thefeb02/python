# 1*2*3*4*5
n = int(input("Enter the number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i


print(f"The factorial of {n} is {factorial}")   
 