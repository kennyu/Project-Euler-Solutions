
with open('42set.txt', 'r') as file:
    words = map(str, file.read().strip().split('"'))
    words = filter( lambda x: x != ',' and x != '', words)

max_len_word =  reduce( lambda x, y: max(x, len(y)), words, 0)

char_to_num_dict = {}
for idx, x in enumerate(range(97, 97+26)):
    char_to_num_dict[chr(x)] = idx+1
    
def convert_to_val(word):
    total = 0
    for c in word:
        total += char_to_num_dict[c] 
    return total
    
triangle_set = set()
for n in  xrange(1, max_len_word*26+1):
    triangle_set.add( n*(n+1) / 2 )
    
triangle_words = 0
for word in words:
    if convert_to_val(word.lower()) in triangle_set:
        triangle_words += 1

print triangle_words
    
