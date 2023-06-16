import math

a=float(input('Δώσε τιμή για το a:'))
b=float(input('Δώσε τιμή για το b:'))
c=float(input('Δώσε τιμή για το c:'))
d=(b**2)-(4*a*c)

if d<0:
    print('Δεν υπάρχουν πραγματικές ρίζες')
elif d==0:
    x=(-b+math.sqrt(b**2-4*a*c))/2*a
    print('Μία λύση:',x)
else:
    x1=(-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2=(-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print('Δύο λύσεις:',x1,'ή',x2)
