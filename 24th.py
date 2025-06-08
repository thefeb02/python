#  *
# ***
# ***** for n = 3

# Print a pyramid pattern of stars for a given number n

n = int(input("Enter the number: "))
for i in range(1, n + 1):
    # Print leading spaces
    print(' ' * (n - i), end='')

    print('*' * (2 * i - 1))
