def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

numb = int(input("Enter a number : "))
if numb < 0:
    print("Factorial is not defined.")
elif numb == 0:
    print("The factorial of 0 is 1")
else:
    res = factorial(numb)
    print(f"The factorial of {numb} is {res}")
