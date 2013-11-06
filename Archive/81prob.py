import math

matrix = open("matrix.txt").read().splitlines()

#for idx,line in enumerate(matrix[0:1]):
#    matrix[idx] = 
    
matrix = map( lambda line: map(int, line.split(',')) , matrix)

row, col = (0,0)

# initialize 

running_sum_row = 0
running_sum_col = 0

for idx in xrange(80):
    running_sum_row += matrix[0][idx] 
    matrix[0][idx] = running_sum_row
    
    running_sum_col += matrix[idx][0]
    matrix[idx][0] = running_sum_col
    
for row in xrange(1,80):
    for col in xrange(1,80):
        matrix[row][col] = matrix[row][col] + min(matrix[row-1][col] , matrix[row][col-1])
        
print matrix[79][79]
    
    

