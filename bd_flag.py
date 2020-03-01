l = input('Enter length of flag: ')
l = int(l)
w = (6/10)*l
r = (1/5)*l
R = l*w
C = 3.1416*r**2
G = R - C
C = round(C,2)
G = round(G,2)
print(f'{C} {G}')
