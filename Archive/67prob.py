file = open('67set.txt', 'r').readlines()
triangle = map( lambda x : map(int, x.strip().split()), file)

for row in reversed(xrange(len(triangle)-1)):
    for idx in xrange(len(triangle[row])):
        triangle[row][idx] += max( triangle[row+1][idx:idx+2] ) 

print triangle[0][0]