'''
Thomas Lockwood
Research
Goal: To find the longest cunningham chain for gaussian integers
'''

#~~~~~~~~~~~~
# Imports
#~~~~~~~~~~~~


import cmath
import math

#############
# is_prime  #
#############

def is_prime(a,b):
    '''
    Is it prime or isn't it prime?
    '''
    if b == 0:
        for i in range(2, int(math.sqrt(abs(a)))+1):
            if a%i == 0:
                return False
        if a%4 == 3:
            return True
    n = a**2 + b**2
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

#########
# cham  #
#########

def cham(a,b):
    '''
    To return the legnth of the cunnigham chain
    (a+bi)*(1+i)+ 1
    '''
    p = complex(a,b)
    c = 0
    while is_prime(p.real, p.imag):
        p = p*(2+1j) + 1+1j
        c += 1
    return c

#########
# main  #
#########

def main():
    q = [0, 1]
    for i in range(1,1000):
        for j in range(1000):
            p = cham(i, j)
            if p >= q[0]:
                q = [p, complex(i,j)]
                print(q)
    return q

main()
#####################
# complex_hailstone #
#####################

def chail(a,b):
    '''
    Hailstone Sequence for complex number 0_0
    '''
    n = complex(a,b)
    cycle = 0
    while n.real != complex(1,0):
        if n.real % 2 == 0 and n.imag% 2 == 0:
            n = n /(complex(2,0))
            n = complex(int(n.real),int(n.imag))
            print(n)
            cycle += 1
        else:
            n = complex(3,0)*n + complex(1,1) 
            n = complex(int(n.real),int(n.imag))
            print(n)
            cycle += 1
        while n.real < 0 and n.imag < 0:
            n = n*1j
    return cycle
        
#chail(3,3)   




# *2, +1
'''
for p*2 + 1
up to 1000
[3, (1+0j)]
[3, (1+20j)]
[3, (1+110j)]
[3, (1+400j)]
[4, (2+1j)]
[5, (4+5j)]
[5, (59+370j)]
[6, (99+830j)]
[6, (939+530j)]
'''

# *1+i, +1
'''
for 1+i*p + 1:
(up to 1000 nothing beats 7)
[3, (1+0j)]
[5, (2+15j)]
[6, (3+82j)]
[7, (7+0j)]
'''
# ..., +i
'''
for 1+i*p + i:
(up to 1000 nothing beast 7
[4, (1+0j)]
[5, (3+98j)]
[5, (8+123j)]
[6, (8+323j)]
[6, (15+22j)]
[6, (150+127j)]
[6, (170+377j)]
[6, (239+260j)]
[6, (275+2j)]
[7, (414+535j)]
'''
# ..., +2+1j
'''
for 1+i*p +2+2j:
(up to 1000)
[2, (1+0j)]
[4, (1+1j)]
[4, (1+2j)]
[4, (1+646j)]
[5, (5+74j)]
[6, (5+94j)]
[6, (6+541j)]
[6, (32+73j)]
[6, (62+343j)]
[6, (77+218j)]
[6, (110+629j)]
[7, (146+71j)]
[7, (440+529j)]
[7, (638+995j)]
[7, (818+155j)]
'''

#*2+i, +1,+i
'''
for 2+i*p + 1
up to 1000:
[1, (1+0j)]
[2, (1+1j)]
'''
# ..., 1+i
'''
for 2+i*p + 1+i
up to 1000
[3, (1+0j)]
[3, (1+4j)]
[4, (1+14j)]
[4, (1+90j)]
[5, (1+110j)]
[5, (2+7j)]
[5, (2+87j)]
[5, (7+2j)]
[5, (7+50j)]
[5, (13+22j)]
[5, (17+12j)]
[5, (17+832j)]
[5, (22+247j)]
[5, (22+455j)]
[5, (31+70j)]
[5, (32+967j)]
[5, (34+449j)]
[5, (34+505j)]
[5, (37+470j)]
[5, (41+90j)]
[5, (43+472j)]
[5, (43+662j)]
[5, (46+895j)]
[5, (47+670j)]
[5, (58+53j)]
[5, (65+96j)]
[5, (70+617j)]
[5, (71+640j)]
[5, (73+682j)]
[5, (74+289j)]
[6, (77+40j)]
[6, (100+883j)]
[6, (212+27j)]
[6, (227+300j)]
[6, (241+640j)]
[6, (302+657j)]
[6, (407+40j)]
[6, (505+502j)]
[8, (560+51j)]
'''

# *2i+1, +1+i
'''
for 2i+1*p +1+i
[3, (1+0j)]
[3, (1+6j)]
[5, (1+40j)]
[5, (1+110j)]
[5, (1+170j)]
[6, (4+469j)]
[6, (345+652j)]
[6, (511+580j)]
[6, (792+103j)]
[7, (967+398j)]
'''
