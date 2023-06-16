lista=[]

while True:
    x = input('Δώσε αριθμό ή r ή 0r ή q:')
    
    if x=='q':
        break
    elif x =='r':
        lista.pop()
    elif x=='0r':
        lista.pop(0)
    elif x[0]=='0':
        x=int(x)
        lista.insert(0,x)
    else:
        x=int(x)
        lista.append(x)
    print(lista)
print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')
