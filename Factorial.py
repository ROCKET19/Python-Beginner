# Program to find the factorial of a number

number = int(input('Enter the number for which factorial is to be determined '))
fact = 1
for count in range(1, number+1):
    fact *= count
print(f"Factorial of {number} is {fact}")