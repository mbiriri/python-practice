#3: factorial using loop

def  factorial_loop(n):
    result=1
    for i in range(1,n+1): # loop from 1 to n
        result*=i

    return result
#test
num=5
print(f"factorial is:",factorial_loop(num))
     