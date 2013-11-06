from eulertools import primes
import itertools

prime_list = filter(lambda x: x >= 1000 and x <= 9999 , map(int, primes(2000)) )
prime_set = set(prime_list)

def is_progression(sequence):
    if len(sequence) != 3:
        return False
    sequence.sort()
    diff = sequence[1] - sequence[0]
    return sequence[2] - sequence[1] == diff

while len(prime_set) != 0:
    prime = prime_set.pop()
    sequence =[]
    for combo in itertools.permutations(str(prime)):
        try:
            elem = int(reduce( lambda x, y: x+y , combo, ''))
            prime_set.remove(elem)
            sequence.append(elem)
        except KeyError:
            continue
    if is_progression(sequence):
        print reduce(lambda x, y: x+y , map(str, sequence), '')
