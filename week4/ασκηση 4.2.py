d_print={}

d_point={'Α':1,'Β':8,'Γ':4,'Δ':4,'Ε':1,'Ζ':10,'Η':1,'Θ':10,'Ι':1,
        'Κ':2,'Λ':3,'Μ':3,'Ν':1,'Ξ':10,'Ο':1,'Π':2,'Ρ':2,'Σ':1,'Τ':1,
        'Υ':2,'Φ':8,'Χ':8,'Ψ':10,'Ω':3}

while True:
    word = input('Δώστε λέξη (ή q για έξοδο): ')
    
    if word == 'q':
        break
    else:
        score = 0
        for letter in word:
            if letter in d_point:
                score += d_point.get(letter)
                d_print[word] = score
        print('Πόντοι Λέξης:',score)

srt = sorted(d_print.items())

print('ΠΕΡΙΕΧΟΜΕΝΑ ΛΕΞΙΚΟΥ')

for key,value in srt:
    print(key,value,end='\n')
print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')
