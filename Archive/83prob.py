matrix = open("83set.txt").read().splitlines()
matrix = map( lambda line: map(int, line.split(',')) , matrix)
graph = {}
        
class Node(object):
    def __init__(self, x , y , val):
        self.x = x
        self.y = y
        self.val = val
        
    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " val: " + str(self.val)  
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " val: " + str(self.val)
    def __hash__(self):
        return hash((self.x, self.y))
        
def node_gen(row, col):
    return Node(row, col, matrix[row][col])
  
for r_idx, row in enumerate(matrix):
    for c_idx, col in enumerate(row):
        graph[node_gen(r_idx, c_idx)] = []

for node in graph.keys():
    row = node.x
    col = node.y
    if col == 0:
        graph[node].append(node_gen(row, col+1))
    elif col == 79:
        graph[node].append(node_gen(row, col-1))
    else:
        graph[node].append(node_gen(row, col+1))
        graph[node].append(node_gen(row, col-1))
        
    if row == 0:
        graph[node].append(node_gen(row+1, col))
    elif row == 79:
        graph[node].append(node_gen(row-1, col))
    else:
        graph[node].append(node_gen(row+1, col))
        graph[node].append(node_gen(row-1, col))  

in_set = {}
def dikstra_alg():
    start = Node(0,0,4445)
    candidates = graph[start][:]
    in_set[start] = start
    for elem in candidates:
        elem.val += start.val
    while candidates:
        while True:
            next = min(candidates, key=lambda x: x.val)
            if next in in_set:
                candidates.remove(next)
                if not candidates:
                    return
            else:
                break
        
        new_cand = graph[next][:]
        elimination_list = []
        for elem in new_cand:
            if elem in in_set:
                elimination_list.append(elem)
            else:
                elem.val += next.val
        for elem in elimination_list:
            new_cand.remove(elem)
        in_set[next] = next
        candidates.remove(next)
        candidates.extend(new_cand)
dikstra_alg()
print in_set[Node(79,79,0)].val      

# Corey fortune 973-256-3772 , 917 753 8489
# Vance Day
#
# Richland equity corporation
# Richard Russell 212 681 9888