penta_list = map( lambda x: x*(3*x-1)/2 , range(1,10000))
penta_set = set(penta_list)
size = len(penta_list)

for idx in xrange(size):
    for idx2 in xrange(idx+1, size):
        p_sum = penta_list[idx] + penta_list[idx2]
        if not p_sum in penta_set:
            continue
        p_diff = penta_list[idx2] - penta_list[idx] 
        if p_diff in penta_set :
            print penta_list[idx] , penta_list[idx2]
            break
    if idx % 1000 == 0:
        print 'Working on...' + str(idx)
        
         #  3(x - y)(x + y) + y -x   == (3*z^2-z)
         #  3x^2 - x + 3y^2 -y == 3*a^2 - a
         #  3(x^2 + y^2) - (x + y) 
         
         # x*(3*x-1) + y*(3*y-1) == z*(3*z-1)
         