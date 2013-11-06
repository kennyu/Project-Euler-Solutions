numbers = open('13set.txt', 'r').readlines()
numbers = map(lambda x: long(x.strip()), numbers)

sum = 0L
for num in numbers:
    sum += num
    
retr = ''
for i in list(str(sum))[0:10]:
    retr += str(i)
    
print long(retr)
