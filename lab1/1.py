import math


numbers = input("Enter number: ").split()

try:
    numbers = [int(i) for i in numbers]
except ValueError:
    print("Invalid input")
    exit()

if len(numbers) < 2:
    print("Please enter at least 2 numbers")
    exit()

result = math.gcd(numbers[0], numbers[1])
for i in range(2, len(numbers)):
    result = math.gcd(result, numbers[i])

print("GCD is: ", result)

