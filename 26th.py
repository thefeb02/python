# WAP to find a greatest number using function
def greatest() :
    c = int(input("Enter the 1st number"))
    b = int(input("Enter the 2nd  number"))
    a = int(input("Enter the 3rd number"))
 
    if(a>b and a>c) :
      return a
    elif(b>a and b>c):
         return b
    else:
        return c

print(greatest())


