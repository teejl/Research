'''
Thomas Lockwood
Goal: Find different Polynomial Permutations
Goddard Research Fall 2014
'''

def solutions(a,p):
    sol = []
    powers = []
    for i in range(a):
        c = i**p % a
        sol.append(c)
        d = set(sol)
        if len(d) == a:
            powers.append(p)
    if len(powers) != 0:
        print powers, 'for', a
    return powers

def multiple_solutions(a,p):
    for i in range(2,p):
        for k in range(a):
            solutions(k,i)

multiple_solutions(1000,100)
