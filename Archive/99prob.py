import math

base_exp = open("99set.txt").readlines()
results = []
for line in base_exp:
    base,exp = line.strip().split(',')
    
    results.append( math.log(int(base),2)*int(exp))
    
print results.index(max(results)) + 1 # match line number
    