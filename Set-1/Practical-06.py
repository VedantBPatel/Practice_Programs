def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
number=int(input("Enter a number you want factorial of: \n"))
print(f"Factorial of {number} is {factorial(number)}")
