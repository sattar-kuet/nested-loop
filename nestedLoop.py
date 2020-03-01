'''for i in range(1,10):
    print(f'outer loop : {i}')
    for j in range(1,4):
        print(f'  inner loop : {j}')'''
#1+(1+2)+ (1+2+3) + (1+2+3+4) + ..
n = input('n=? : ')
n = int(n)
for i in range(1,n+1):
    if i>1:
      print('(',end='')
    for j in range(1,i+1):
        if j==i:
           print(f'{j}',end='')
        else:
            print(f'{j}+', end='')
    if i>1:
      print(')+',end='')
print('...',end='')