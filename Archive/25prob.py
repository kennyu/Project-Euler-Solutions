
a = 1
b = 1
n = 2

while True:
    n += 1
    if a >= b:
        b += a
        if len(str(b)) == 1000:
            break
    else:
        a += b
        if len(str(a)) == 1000:
            break
print n
            
