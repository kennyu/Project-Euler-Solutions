def is_cancelling_frac(num, denom):
    a = set(str(num))
    b = set(str(denom))
    intersect_set = a.intersection(b)
    if not intersect_set or num >= denom:
        return False
    for elem in intersect_set:
        top = list(str(num))
        top.remove(elem)
        bot = list(str(denom))
        bot.remove(elem)
        top = float(reduce(lambda x,y : x+y, top, ''))
        bot = int(reduce(lambda x,y : x+y, bot, ''))
        try:
            if top/bot == float(num)/denom:
                return True
        except:
            continue
    return False

mult = 1
for num in xrange(10 , 100):
    for denom in xrange(10, 100):
        if num % 10 == 0 and denom % 10 == 0:
            continue
        if is_cancelling_frac(num, denom):
            mult *= (float(num)/denom)
           
''' Find the last decimals place (ie hundreth, thousanth ) '''
print 10**len(str(mult % 1)[2:])