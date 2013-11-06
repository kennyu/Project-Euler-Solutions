file = open('8set.txt', 'r').readlines()

large_line = ''
for line in file:
    large_line += line.strip()
    
curr_largest = 0
large_line = map(int,(list(large_line)))
for idx, num in enumerate(large_line[:-4]):
    prod = num 
    for index in range(idx+1, idx+5):
        prod *= large_line[index]
    if prod > curr_largest:
        curr_largest = prod
   
print curr_largest