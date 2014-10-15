# Thomas Lockwood
# Polynomial Permutations with Gaussian Integers

'''
This program is designed to find out where the residues shift whenever
applied by a linear transformation x^n
'''

#_________________#
# imports
#_________________#

import cmath
import fractions

#_________________#
# listit
#_________________#

def reslist(r,i):
    '''
    r + ij is the modulis we will be working with
    return the list of residues
    '''

    residues = []
    
    for a in range(r+1):
        for b in range(i+1):
            residues.append([a,b])
    del residues[-1]
##    print(residues)
    return(residues)

#_________________#
# shift
#_________________#

def shift(n, r, i):
    '''
    r + ij is the modulis
    n is the power of the polynomial
    return the new list of residues while printing both in and out
    '''

    before = reslist(r,i)
    new = []
    for item in before:
        x,y = item
        v = complex(x,y)**n
        v = v%complex(r,i)
        x = int(v.real)
        y = int(v.imag)
        while abs(x) > r or abs(y) > i or x < 0 or y < 0 :
            v = (complex(x,y)*1j)%complex(r,i)
            x = int(v.real)
            y = int(v.imag)
            print(v)
            
        new.append([x,y])
        
    mapped = zip(before,new)
    for item in mapped:
        print(item)

    return new


#_________________#
# check
#_________________#

def check(r,i):
    '''
    r + ij will be the modulus
    checking powers up to the norm that work
    to be cont... [ the point of this program is to check the powers/scalars
    that will produce an linear transformation]
    '''
    n = int(r**2 + i**2)
    for a in range(1,n):
        print(a)
        shift(a,r,i)
        print()
        print()


####    n = int(r**2 + i**2)
####    u = reslist(r,i)
####    pps = []
####    
####    for a in range(1,n):
####        v = shift(a,r,i)
####        flag = True
####        
####        for item in u:
####            if item not in v:
####                flag = False
####        if flag == True:
####            pps.append(a)
####            
####    print(pps)
####    return pps
####
check(5,2)


'''
after producing the number of numbers that make a linear transformation my next
objective will be to produce a map each one and classify which groups align up
to produce the same linear transformation/ anyway i can relate the transformations
'''
              
