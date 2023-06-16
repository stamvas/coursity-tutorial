p1=float(input('Δώσε γεωγραφικό πλάτος 1:'))
m1=float(input('Δώσε γεωγραφικό μήκος 1:'))

p2=float(input('Δώσε γεωγραφικό πλάτος 2:'))
m2=float(input('Δώσε γεωγραφικό μήκος 2:'))

R=6372.8

import math

dp=math.fabs(p2-p1)
dm=math.fabs(m2-m1)
dp=math.radians(dp)
dm=math.radians(dm)

a=math.sin(dp/2)**2+ math.cos(p1)*math.cos(p2)*math.sin(dm/2)**2
c=2*math.asin(math.sqrt(a))
d=R*c

print(round (d,-2))
