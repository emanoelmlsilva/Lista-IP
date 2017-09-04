A = float(input())
B = float(input())
C = float(input())

D = (B**2)-(4*A*C)
E = D**(1/2)
if((D < 0) or (A == 0)):
    print('Impossivel calcular')
else:
    r1 = (-B + E)/(2*A)
    r2 = (-B - E)/(2*A)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
    

