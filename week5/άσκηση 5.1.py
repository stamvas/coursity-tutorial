import random,math

def stats(L):
    M = sum(L)/N
    S = 0
    
    for i in range(N):
        S+=(L[i]-M)**2
        sd = math.sqrt((1/(N-1)*S))
    
    print('Πλήθος ακεραίων στη λίστα:',N)
    print('Λίστα:',L)
    print('Μέσος όρος : {:.2f} , Τυπική απόκλιση : {:.2f}'.format(M,sd))  

N=int(input('Δώσε τιμή για το Ν:'))
L=[]

for i in range(N):
    L.append(random.randint(1,20))
stats(L)

print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')
