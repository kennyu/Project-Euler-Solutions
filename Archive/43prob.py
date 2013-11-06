import itertools

property_num = []

def has_property(n):
    
    if  int(n[3])%2 ==0 \
    and int(n[7:10]) % 17 == 0 \
    and int(n[5])%5 == 0 \
    and sum( map(int, list(n[2:5]))) % 3 ==0 \
    and int(n[4:7]) % 7 == 0 \
    and int(n[5:8]) % 11 == 0 \
    and int(n[6:9]) % 13 == 0 :
        return True
        
    return False
    
def to_int(n):
    return int(to_str(n))
    
def to_str(n):
    return ''.join(map( str, n))
    
for num in itertools.permutations(range(10)):  
    if has_property(to_str(num)):
        property_num.append(to_int(num))
    
print sum( property_num )

# 16695334890

