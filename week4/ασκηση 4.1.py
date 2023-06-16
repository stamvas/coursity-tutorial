di={}

while True:
    x = input('Δώσε ΑΜ και όνομα μαθητή ή q για έξοδο ')
    
    if x == 'q':
        break
    else:
        x.split(',')
        AM,name = x.split(',')
        AM = int(AM)
        di[AM] = name
        list(di.keys())
        srt = sorted(di.items())

print('ΠΕΡΙΕΧΟΜΕΝΑ ΛΕΞΙΚΟΥ')

for key,value in srt:
    print(key,value,end='\n')
print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')
