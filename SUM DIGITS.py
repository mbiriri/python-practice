#6: sum of digits 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   # get last digit
        n //= 10          # remove last digit
    return total

# Example usage
num = 1234
print(f"Sum of digits of {num} is:", sum_of_digits(num))