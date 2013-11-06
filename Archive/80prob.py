from decimal import *

elem_list = range(1,101)
count = 0

getcontext().prec = 200
getcontext().rounding = ROUND_DOWN

for i in xrange(1,101):
    try:
        elem_list.remove(i**2)
    except:
        pass
 
zt = 0
for number in elem_list:
    a = Decimal.sqrt(Decimal(number))
    a = list(str(a))[0:101]
    a.remove('.')
    count += sum(map(int, a))
  
    

print count