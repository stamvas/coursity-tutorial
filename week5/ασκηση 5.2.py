def myrange(N,logos):
    i=0
    j=1
    while i<N :
        yield j
        i+=1
        j=j*logos
        
for i in myrange(5,10):
    print(i)

print()

for i in myrange(6,2):
    print(i)
print('\nΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')
