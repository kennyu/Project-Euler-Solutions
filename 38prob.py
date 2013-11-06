from itertools import count

def is_pandigital(num_string):
    return len(num_string) == 9 and len(set(num_string)) == 9 and not '0' in set(num_string)
   
pandigital_list = []
for x in xrange(1, 10001):
    num_string = ''
    for n in count(1):
        num_string += str(n*x)
        if len(num_string) >= 9:
            break
    if is_pandigital(num_string):
        print num_string
        pandigital_list.append((int(num_string),x))
        
a = max(pandigital_list, key = lambda x: x[0])
print a
