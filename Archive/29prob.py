
seq_set = set()
for a in xrange(2,101):
    for b in xrange(2,101):
        seq_set.add(a**b)
print len(seq_set)   
