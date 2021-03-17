x = 5

print(x==2)
print(x==5)
print(x!=5)
print(x!=213)
print(x>14)

#############################
imie = "Bob"
nazwisko = 'Bobowsky'
wiek = 30

if nazwisko == 'Bobowsky' and wiek == 31:
    print('Czesc Bobowsky, masz 30 lat')
else:
    print('to nie ty')

if imie in ['Bob','Krzysztof'] and wiek == 30:
    print('Czesc Bob, masz 30 lat')
else:
    print('to nie ty')

############################
zmienna1 = -1
zmienna2 = 2
zmienna3 = 3

if zmienna1 > 0:
    print('1')
elif zmienna2 == 2:
    print('2')
else:
    print('same falsy')