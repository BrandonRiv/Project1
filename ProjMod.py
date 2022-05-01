'''
This function accepts a positive integer
Returns the sum of all integers from 1 up to the number passed
'''
def one(n) -> int:
    if n == 1:
        return 1
    else:
        return n + one(n-1)


'''
This function accepts two positive integers
First being the number raised, represented by num
Second being the power, represented by pow
'''
def two(num, pow) -> int:
    if pow == 0:
        return 1
    elif pow == 1:
        return num
    else:
        return num * two(num, pow - 1)


'''
This function accepts a positive integer
Prints out all the numbers from the number passed up to 1
'''
def three(n3) -> int:
    if n3 > 0:
        print(n3, end=' ')
        return three(n3-1)



