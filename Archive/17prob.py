import itertools

digits = ['','one','two','three','four','five',
           'six', 'seven','eight','nine']

tens = ['','', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']
           
sp = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
      'fifteen', 'sixteen', 'seventeen', 'eighteen',
      'nineteen']
      
count = 0

def parse_number(num):
    global count
    num_list = list(str(num))
    numbers = map(int, num_list)
    it = itertools.izip(xrange(len(numbers),0,-1), numbers)
    for pos, x in it :
        if pos == 4:
            add_to_count('one','thousand')
            break
        elif pos == 3:
            add_to_count(digits[x], 'hundred') 
            if not (numbers[-1] == 0 and numbers[-2] == 0):
                add_to_count('and')
            
        elif pos == 2:
            if  x == 1:
                add_to_count(sp[numbers[-1]])
                break
            else:
                add_to_count(tens[x]) 
        elif pos == 1: 
            add_to_count(digits[x])
            
def add_to_count(*strings):
   # print strings
    global count
    for s in strings:
        count += len(s)
        
for x in xrange(1,1001):
    parse_number(x)
print count