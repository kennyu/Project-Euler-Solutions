file = open('18set.txt', 'r').readlines()
triangle = map( lambda x : map(int, x.strip().split()), file)

for row in reversed(xrange(len(triangle)-1)):
    for idx in xrange(len(triangle[row])):
        triangle[row][idx] += max( triangle[row+1][idx:idx+2] ) 

print triangle[0][0]

# DIKJSTRA IMPLEMENTATION BECAUSE I WAS A CRAZY , THIS DOESN'T WORK FOR LONGEST PATH :(
# import copy
# graph = {}

# def build_graph(graph):
    # start = None
    # for row in xrange(len(triangle)):
        # for idx in xrange(len(triangle[row])):
            # if row == 0 and idx == 0:
                # start = node_gen(0,0)
            # if row < len(triangle)-1:
                # graph[ node_gen(row,idx)] = [ node_gen(row+1 , idx) , node_gen(row+1, idx+1) ]
            # else:
                # graph[ node_gen(row,idx)] = []
    # return start
    
# class Node(object):
    # def __init__(self, row , idx, val):
        # self.id = (row, idx)
        # self.val = val
        
    # def __eq__(self, other):
        # return self.id == other.id
        
    # def __hash__(self):
        # return hash(self.id)
    
    # def __repr__(self):
        # return "id: " + str(self.id) + " val: " + str(self.val)  
        
    # def __str__(self):
        # return "id: " + str(self.id) + " val: " + str(self.val)  
        
# def node_gen(row, idx):
    # return Node(row, idx, triangle[row][idx])
            
# start = build_graph(graph)


#def dikstra_alg(start, graph):
#    in_set = set()
#    in_set.add(start)
#    candidates = copy.deepcopy(graph[start])
#    for elem in candidates: elem.val += start.val
#    while candidates:
    #    get largest node in candidates
#        node = min(candidates, key = lambda x : x.val)
    #    mark as added
#        in_set.add(node) 
    #    remove node from candidates
#        candidates = filter(lambda x: node != x, candidates) 
    #    get new candidate list
# `      new_candidates = filter( lambda x: not x in in_set , copy.deepcopy(graph[node]))
    #    update their values
#        for elem in new_candidates: elem.val += node.val
    #   add to candidate list
#        candidates.extend( new_candidates )
#    return [ elem for elem in in_set if graph[elem] == [] ]