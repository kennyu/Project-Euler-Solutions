my_list = []
for a in xrange(1000):
    if a*3 <1000:
        my_list.append(a*3)
    if a*5 < 1000:
        my_list.append(a*5)

print sum(set(my_list))