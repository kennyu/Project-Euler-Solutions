from eulertools import primes
from itertools import count
''' Create prime set for prime checking '''
# prime_set = set(primes(10**8))

''' Starting from 1 , to reach next diagonal number, add (2s, 4s, 6s,...) four times '''
primes_seen = 0
current_num = 1
diagonals_seen = 1

def parse(n):
    global primes_seen, current_num, diagonals_seen
    for x in xrange(4):
        current_num += 2*n
        diagonals_seen += 1
        if is_prime(current_num):
            primes_seen += 1
    
    if primes_seen / float(diagonals_seen) < .1:
        print 2*n + 1
        return -1
        
def is_prime(n):
    if n <= 1 :
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    counter = 3
    while (counter * counter ) <= n:
        if n % counter == 0:
            return False
        else:
            counter += 2
    return True
  
# print is_prime(2) == True  
# print is_prime(3) == True
# print is_prime(4) == False
# print is_prime(5) == True
# print is_prime(8) == False
# print is_prime(9) == False
   
for n in count(1):
    if parse(n) == -1:
       break
 
        