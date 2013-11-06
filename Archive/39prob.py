import math
p_dict = {}

for a in xrange(1,1000):
    for b in xrange(a, 1000):
        if a+b > 1000:
            break
        pythag_trip = [ a , b, math.sqrt(a**2 + b**2)]
        try:
            p_dict[sum(pythag_trip)] += 1
        except:
            p_dict[sum(pythag_trip)] = 1
            
print max( [( x , p_dict[x]) for x in p_dict if x < 1000 and x % 1 == 0], key = lambda x: x[1])