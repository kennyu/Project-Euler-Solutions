with open('22set.txt', 'r') as file:
    names = map(lambda x: x.strip('"').lower(), file.read().strip().split(','))
    names.sort()
    
alph_dict = {}
for a in xrange(97, 97+26):
    alph_dict[chr(a)] =  a - 96
    
def name_to_int(n):
    score = 0
    for char in n:
        score += alph_dict[char]
    return score
    
total = 0
for idx, name in enumerate(names):
    total += (idx+1)*name_to_int(name)
  
print total