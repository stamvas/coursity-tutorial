import random

N=int(input('Δώσε τιμή για το Ν:'))
lista=[]

for i in range(N):
    lista.append(random.randint(1,100))

for i in range(N):
    for j in range(N-1):
        if lista[j+1]<lista[j]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

print(lista)
print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')
