# 5: factorial using recursion

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# TEST
num = 5
print(f"Factorial of {num} is:", factorial_recursive(num))