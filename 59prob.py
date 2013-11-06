with open('59set.txt','r') as file:
    code = map( int, file.read().strip().split(','))
    
''' Split into 3 sets for each for 3 passcode cases '''
a = code[0::3]
b = code[1::3]
c = code[2::3]
sets = a, b, c

''' Assume that space is the most common character in the decoded set
sort above sets and find int that XORs with top number '''

keys = []
for num_set in sets:
    num_count = [ (x , num_set.count(x)) for x in set(num_set) ]
    top_num = max(num_count, key = lambda x: x[1])[0]
    for c in xrange(0, 256):
        if chr(c ^ top_num) == ' ':
            print c, chr(c)
            keys.append(c)
            break

for idx, c in enumerate(code):
    code[idx] = c ^ keys[idx % 3]
    
print sum(code)