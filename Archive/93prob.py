import itertools
def add(a,b): return a+b
def sub(a,b): return a-b
def mult(a,b): return a*b
def div(a,b): return float(a)/b

best_combo = [(1,2,3,4), 28]

def check_longest_run(list, combo):
    global best_combo
    list.sort()
    n = 0
    for a in list:
        if a <= 0 or a < n+1:
            pass
        elif a == n+1:
            n += 1
        else:
            if n > best_combo[1]  :
                best_combo[0], best_combo[1] = combo, n
                
op_combo = [p for p in itertools.product([add,sub,div,mult] , repeat=3)]

for numbers in itertools.combinations(range(1,10), 4):
    num_combo = list(itertools.permutations(numbers))
    my_list = []
    for ops in op_combo:
        for nums in num_combo:
            my_list.append( ops[0](ops[1]( ops[2](nums[0] , nums[1]) , nums[2] ), nums[3] ))
            my_list.append( ops[0](ops[1](nums[0] , nums[1]) , ops[2](nums[2] , nums[3])) )
    check_longest_run(my_list, numbers)

print best_combo

# Testing would have really helped