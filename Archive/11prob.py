from operator import mul

matrix = open('11set.txt', 'r').readlines()
matrix = map( lambda line: map(int, line.split()) , matrix)

def go_through_row():
    global n
    for r_idx, row in enumerate(matrix):
        for c_idx in xrange(len(row)):
            product = reduce(mul,row[c_idx:c_idx+4],1)
            n = max( product, n )

def go_through_diag():
    global n
    for r_idx, row in enumerate(matrix):
        for c_idx in xrange(len(row)):
            try:
                diag = [matrix[r_idx+i][c_idx+i] for i in xrange(4)]
                product = reduce ( mul, diag,1 )
                n = max( product, n)
            except:
                break
n = 0
go_through_row()
go_through_diag()  
map(list.reverse, matrix)
go_through_diag() 
map(list.reverse, matrix) 
          
matrix = map(list, zip(*matrix))
go_through_row()

print n
