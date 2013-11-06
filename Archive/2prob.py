
fib_a = 1
fib_b = 1
sum = 0

while fib_a + fib_b < 4000000:
    fib_n = fib_a + fib_b
    if fib_n%2 == 0:
        sum += fib_n
    if fib_a > fib_b:
        fib_b = fib_n
    else:
        fib_a = fib_n
        
print sum
