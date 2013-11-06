def tria(n): return n*(n+1)/2
def squa(n): return n*n
def pent(n): return n*(3*n-1)/2
def hexa(n): return n*(2*n-1)
def hept(n): return n*(5*n-3)/2
def octa(n): return n*(3*n-2)
    
eqs = [tria, squa, pent, hexa, hept, octa]
sets = [{} for x in xrange(len(eqs))]

for x in xrange(1,200):
    for idx, func in enumerate(eqs):
        result = func(x)
        if len(str(result)) == 4 and result % 100 > 9:
            try:
                sets[idx][result/100].append(result)
            except:
                sets[idx][result/100] = []
                sets[idx][result/100].append(result)

def recurse_crawl(start,curr_n, data):
    if len(data['path']) == 6 and curr_n % 100 == start / 100:
        print sum(data['path'])
        print data
    for idx, set in enumerate(sets):
        if not idx in data['visited_set']:
            try:    
                next_num_set = set[curr_n % 100]
                for num in next_num_set:
                    data['visited_set'].append(idx)
                    data['path'].append(num)
                    recurse_crawl(start, num, data)
            except:
                continue
    data['visited_set'].pop()
    data['path'].pop()

for keys in sets[0]:
    for start in sets[0][keys]:
        recurse_crawl( start, start, {'path':[start] , 'visited_set':[0]} )
        