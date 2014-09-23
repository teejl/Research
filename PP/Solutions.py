'''
Thomas Lockwood
Goal: Find different Polynomial Permutations
Goddard Research Fall 2014
'''

def Solutions(a,p):
    sol = []
    for i in range(a):
        c = i**p % a
        sol.append(c)
    return sol
