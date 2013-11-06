def is_palindrome(n):
    ''' n is int, we convert it to string and binary string'''
    a = str(n)
    b = bin(n)[2:]
    if n == 1 or n == 3 or n == 5 or n == 7 or n == 9:
        return True
    return a[:len(a)/2][::-1] == a[-int(len(a)/2):] \
    and b[:len(b)/2][::-1] == b[-int(len(b)/2):] 

sum = 0

for x in xrange(1,10**6):
    if is_palindrome(x):
        sum += x
        
print sum 