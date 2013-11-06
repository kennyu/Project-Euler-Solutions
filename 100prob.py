# condition: y > 10**12
# solve this equality: x ( x - 1) 2 = y ( y - 1 )
import math

y = 10**12 + 1
x = int(math.sqrt(y^2 / 2))

while True:
    y_frmla = y*(y-1)
    x_frmla = x*(x-1)*2
    if y_frmla > x_frmla:
        x += 1
    elif y_frmla < x_frmla:
        y += 1
    else:
        print x
        break
    
# x = 3312555
# y = 4684660


