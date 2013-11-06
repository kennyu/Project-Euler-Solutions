largest_palin = 0 
def is_palindrome(num):
    mid = (len(num)-1)/2
    for a in xrange(mid+1):
        if num[a] != num[-1*(a+1)]:
            return False
    return True
    
for a in xrange(100,1000):
    for b in xrange(100,1000):
        if is_palindrome(list(str(a*b))):
            if a*b > largest_palin:
                largest_palin = a*b
print largest_palin