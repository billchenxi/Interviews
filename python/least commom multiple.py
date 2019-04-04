# Example input() statement
number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))

# Use print() to print the result, like this:

def gcd(a, b):
    while (b != 0):
        t = a       # set aside the value of a
        a = b       # set a equal to b
        b = t % b   # divide t (which is a) by b

    return a
LCM = number1 * number2 /  gcd ( number1 , number2 )
print(LCM)