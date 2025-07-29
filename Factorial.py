def factorial(n):
    
    if n == 1:
        print(n)
        return 1 #base case
    else:
        print (n,'*',end=' ')
        return n * factorial(n-1) #recursive case
    
n = 2
print('factorial of', n, factorial(n))
    
    