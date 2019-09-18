import requests

alphabet = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
c = 0

for letter1 in alphabet:
    for letter2 in alphabet:
        if requests.get('https://www.github.com/'+letter1+letter2+'/').status_code == 404:
            print('!!!', letter1+letter2)
            quit()
    print(c)
    c += 1

for digit in digits:
    for letter in alphabet:
        if requests.get('https://www.github.com/'+digit+letter+'/').status_code == 404:
            print('!!!', digit+letter)
            quit()
        print(digit+letter)
    print(c)
    c += 1

for letter in alphabet:
    for digit in digits:
        if requests.get('https://www.github.com/'+letter+digit+'/').status_code == 404:
            print('!!!', letter+digit)
            quit()
        print(letter+digit)
    print(c)
    c += 1
