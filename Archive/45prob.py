triag = set()
penta = set()
hexa  = set()

for x in xrange(143,1000000):
    triag.add(x*(x+1)/2)
    penta.add(x*(3*x-1)/2)
    hexa.add(x*(2*x-1))

print triag & penta & hexa