import random

red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,29,31,33,35]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,30,32,34,36]

while True:
    roulette=random.randint(0,36)
    print(roulette)
    
    if roulette<=18:
        print('Μικρός αριθμός')
    else:
        print('Μεγάλος αριθμός')

    if roulette==0:
        print('Κληρώθηκε το 0')
    elif roulette in red:
            print('Κοκκινος αριθμός')
    else:
              print('Μαύρος αριθμός')

    if roulette==0:
        print('Κληρώθηκε το 0')
    elif roulette%2==0:
        print ('Κληρώθηκε ζυγός αριθμός')
    else:
        print('Κληρώθηκε μονός αριθμός')

    inp = input('Enter: Συνέχεια, q: Έξοδος ')
    
    if inp=='q':
        break
    
