n =int((input("Enter the number:")))
for i in range(2, n):
    if n % i == 0:
        print(f"{n} iscomposite") 
        break
    else:
        print(f"{n} is prime ")
        break