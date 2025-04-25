#2: check if number is even or odd

def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

#test
num=7
print(f"the number 7 is:",even_odd(num))
