coinage = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_recur(last_coin_idx, amount):
    if last_coin_idx <= 0 or amount <= 0:
        return 1
        
    total = 0
    if not amount - coinage[last_coin_idx] < 0:
        total += coin_recur(last_coin_idx, amount - coinage[last_coin_idx])
    
    total += coin_recur(last_coin_idx-1, amount)
        
    return total
    
print coin_recur(len(coinage)-1, 200)