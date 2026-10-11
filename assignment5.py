'''Ask the user to enter two numbers.

Display their:

Sum and difference

Product and quotient

Floor division and remainder

First number raised to the power of the second

Example: if the numbers are 10 and 3, the remainder should be 1.

Challenge: What happens if the second number is zero? Prevent division-by-zero errors using a condition.'''

a=int(input('frist number: '))
b=int(input('second number: '))
print('sum:', a+b)
print('difference:', a-b)
print('multipication:', a*b)
print('quotient:', a/b)
print('floor division:', a//b)
print('remainder:', a%b)
print('power of:', a**b)