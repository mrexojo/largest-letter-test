import numpy as np

def solution (S):

    spl= []
    upandlow= []
    mayus=''

    for letter in S:
        spl.append(letter)
    
    for l in spl:
        if l.isupper():
            mayus=l
            check=mayus.lower()
            for j in spl:
                if check == j:
                    upandlow.append(j)

    if not upandlow:
        print("NO")
        return

    arr= np.array(upandlow)
    lista = arr.tolist()
    rlista= sorted(lista,reverse=True)
    print(rlista[0].upper())

income=input('type a string: ')
alpha = income.isalpha()
tincome = len(income)
letters = 200000

if tincome < letters and alpha:
    solution(income)
else:
    print(f'Sorry, It require letters with a max of {letters} letters')
