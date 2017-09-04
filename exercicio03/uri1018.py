n = int(input())
c = 100
l = 50
t = 20
x = 10
v = 5
d = 2
u = 1
if((n>0) and (n<1000000)):
    resc = n // c
    n = n%c
    resl = n // l
    n = n%l
    rest = n // t
    n = n%t
    resx = n // x
    n = n%x
    resv = n // v
    n = n%v
    resd = n // d
    n = n%d
    resu = n
print('{} nota(s) de R$100,00'.format(resc))
print('{} nota(s) de R$50,00'.format(resl))
print('{} nota(s) de R$20,00'.format(rest))
print('{} nota(s) de R$10,00'.format(resx))
print('{} nota(s) de R$5,00'.format(resv))
print('{} nota(s) de R$2,00'.format(resd))
print('{} nota(s) de R$1,00'.format(resu))
