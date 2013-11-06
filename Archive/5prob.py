factor = 19*17*13*11
p = [60, 18, factor, 16, 14, 12]
num = factor

def is_even_div(num):
    for a in p:
        if num % a != 0:
            return False
    return True
    
while True:
    if is_even_div(num):
        break
    else:
        num += factor
        
print num