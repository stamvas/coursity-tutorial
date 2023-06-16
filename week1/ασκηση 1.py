
x=int(input('Δώσε τιμή X:'))
y=int(input('Δώσε τιμή Y:'))

import math

p1=int(x)/int(y)
p2=int(x)%int(y)
p3=math.log(x)/math.log(y)
p4=math.sqrt(y)
p5=math.exp(x)

print('{:10.3f}{:10.3f}{:10.3f}{:10.3f}{:>10.3f}'.format(p1,p2,p3,p4,p5))

