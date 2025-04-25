def sum_list(*args):
    total=0
    for i in args:
        total+=i # add each number to total
    return total

#test
result=sum_list(2,4,6,7)
print(result)
