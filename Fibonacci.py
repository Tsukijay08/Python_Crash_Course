def fibonacci_n(n):
    if 0 <= n <= 30:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    else:
        print("Input must be between 0 and 30 (inclusive).")
    

# Example usage:
n = 40
print(f"F({n}) =", fibonacci_n(n))
    
 

        
        