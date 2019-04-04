# def fib(n):
#     # generate the first n Fibonacci numbers
#     i = 0
#     last = 0
#     current = 1
#     while i < n:
#          yield current
#          temp = current + last
#          last = current
#          current = temp
#          i += 1

# print([*fib(10)])

# Example input() statement
number = 6

# Use print() to print the result, like this:
def s(n):  
    i = 0
    next_i = 2*i +1
    while i <= n:
        yield next_i
        next_i = 2*next_i +1
        i += 1
results = [*s(number)]

print(results[-1])


