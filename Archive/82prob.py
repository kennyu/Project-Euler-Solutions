matrix = open("83set.txt").read().splitlines()
matrix = map( lambda line: map(int, line.split(',')) , matrix)
        
def change_row(row_target, col):
    if row_target == len(matrix):
        matrix[row_target][col] += min( matrix[row_target][col-1] , matrix[row_target-1][col] )
        return 
    if row_target == 0:
        curr_min = matrix[row_target][col-1]
    else:
        curr_min = min( matrix[row_target][col-1] , matrix[row_target-1][col])
    running_sum = 0
    for row in matrix[row_target+1:]:
        running_sum += row[col]
        curr_min = min( curr_min , row[col-1] + running_sum )
    matrix[row_target][col] += curr_min 

for col in xrange(1 , 80):
    for row in xrange(len(matrix)):
        change_row( row , col)
        
print min(map( lambda x: x[-1:] , matrix ))

def test_init():
    return map( lambda x: x[0] , matrix )[0:2] == [ 4445 , 4445+1096 ] 

def test_first_col():
    return map( lambda x: x[1] , matrix )[0] == 2697 + 20 + 1096


