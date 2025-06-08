cmnt=["make a lot of money","Buy Now","suscriibe this","click this"]

spam =input("Enter the comment : ").lower()
if spam in cmnt:
    print("This is spam")
else:
    print("This is not spam")