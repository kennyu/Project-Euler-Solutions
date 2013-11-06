def collatz(x):
    n = 1
    while x != 1:
        n += 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x+1
    return n

chain = [1,1]
for x in xrange(2,1000000):
    print x
    seq_len = collatz(x)
    if chain[1] < seq_len :
        chain[0], chain[1] = x, seq_len
print chain[0]