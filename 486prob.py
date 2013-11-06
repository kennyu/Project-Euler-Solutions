import random

def whoWins():
    a = 0
    b = 0
    count = 0
    while count < 2:
        while count < 1:
            a = random.random()
            count += a
        b = random.random()
        count += b
    return b > a
  
runs = 1000000000
snd_wins = 0
for a in xrange(runs):
    if whoWins():
        snd_wins += 1
        
        
print float(snd_wins) / runs