
for a in xrange(1,1000):
    for b in xrange(a+1,1000):
        for c in xrange(b+1,1000):
            if a**2 + b**2 == c**2 and a+b+c==1000:
                return a*b*c