# test
# pandas + numpy + matplotlib/seaborn
# netmico + paramico
#
# print('whatever')
# print('cos jeszcze')
# przerwa do 10:11
# print("hello!")
# print('hello!')
# print("Mc'Donalds")
# x='Andrzej'
# y=10
# print(x)
# print(y)
# print('Witaj '+x+"!")
# print('Witaj {}!'.format(x))
# print(f'Witaj {x}!')
# print(type(y))
# print('y='+str(y))
# print('y={}'.format(y))
# print(f'y={y}')
# owoc=input('podaj swój ulubiony owoc:\n')
# print(f'Twój ulubiony owoc to {owoc}')
# print('Twój ulubiony owoc to {}'.format(owoc))
# print('Twój ulubiony owoc to '+owoc)

# 1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
#   wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
#
# imie=input('podaj imię:\n')
# nazwisko=input('podaj nazwisko:\n')
# print(f'Witaj {imie} {nazwisko}!')
# print('Witaj {} {}!'.format(imie,nazwisko))
# print('Witaj '+imie+" "+nazwisko+"!")

# print(imie+" "+nazwisko)

# x=input('dej x:\n')
# y=input('dej y:\n')
# print(x,type(x))
# print(y,type(y))
# #print(x/y)

# x=float(input('dej x:\n'))
# y=float( input('dej y:\n') )
# print(x,type(x))
# print(y,type(y))
# wynik=round(x/y,2)
# print(wynik)
# print(pow(2,10))

# 2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę w kilogramach
# i wzrost w metrach, wyliczy i wypisze BMI.

# wzrost=1.76

# wzrost = float(input('podaj wzrost w metrach:\n'))
# masa = float(input('podaj masę w kilogramach:\n'))
# bmi=round(masa/pow(wzrost,2),2)
# print(f'bmi={bmi}')
#

#
# x=1
# if x == 1:
#     print('jeden')
#     print('jeden')
#     print('jeden')
# print('koniec')


# x=2
# if x == 1:
#     print('jeden')
# else:
#     print('nie jeden')
# print('koniec')

# x=2
# if x == 1:
#     print('jeden')
# elif x==2:
#     print('dwa')
# elif x==3:
#     print('trzy')
# else:
#     print('poza zakresem')
# print('koniec')
#
# x=1
# y=1
# if x==1:
#     print('x=1')
# if y==1:
#     print('y=1')

#3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość z informacją "wartość dodatnia",
# jeśli zero to wyświetlamy z informacją "równe zero", jeśli ujemna to wyświetlamy "wartość ujemna".

# liczba=float(input('podaj jakąś liczbę:\n'))
# if liczba<0:
#     print(f'{liczba} jest ujemna')
# elif liczba==0:
#     print(f'{liczba} jest zerem')
# else:
#     print(f'{liczba} jest dodatnia')

# liczba=int(input('podaj jakąś liczbę:\n'))
# if liczba<0:
#     print(f'{liczba} jest ujemna')
# elif liczba==0:
#     print(f'{liczba} jest zerem')
# else:
#     print(f'{liczba} jest dodatnia')


#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
#
# wzrost = float(input('podaj wzrost w metrach:\n'))
# masa = float(input('podaj masę w kilogramach:\n'))
# bmi=round(masa/pow(wzrost,2),2)
# print(f'bmi={bmi}')
# if bmi<16:
#     print('wygodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa ok')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('przypakowanie I stopnia')
# elif bmi<40:
#     print('przypakowanie II stopnia')
# else:
#     print('przypakowanie III stopnia')

#przerwa do 11:31

# for x in range(10):
#     print('siema!')
# #
# # while 1==1:
# #     print('siema!')
#
# while True:
#     print('prawda!')

# for x in range(3):
#     print('wykonanie!')
#
# for x in range(3):
#     print(f'wykonanie {x}')


# for x in range(1,11):
#     print(f'wykonanie {x}')
#
# for x in range(1,11,2):
#     print(f'wykonanie {x*10}')

#5. Wyświetl 20 kolejnych potęg liczby 2

#print(pow(2,x))

# for x in range(1,21):
#     print(x,pow(2,x))

# for x in range(-10,11):
#     if x<0:
#         print(f'{x} jest ujemne')
#     elif x==0:
#         print(f'{x} jest zerem')
#     else:
#         print(f'{x} jest dodatnie')

#print(11%2)

#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta
#
# for e in range(1,101):
#     if e%2==0:
#         print(f'{e} jest parzyste')
#     else:
#         print(f'{e} jest nieparzyste')
#
# print(e)
    #print(e)

# def funkcja():
#     zmienna=0
#7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
  # - kwotę lokaty
  # - oprocentowanie w skali roku
  # - ilość miesięcy na jaką zakladamy lokatę
  # Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
  # oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
  # Kapitalizacja comiesięczna
#
# kwota=100000
# oprocentowanie=0.08
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     kwota=kwota+(kwota*oprocentowanie/12)
#     print(m,round(kwota,2))

# while True:
#     print('true!')
#
# while 1==1:
#     print('true!')
#
# x=0
# suma=0
# while suma<=100:
#     print(f'x={x} suma={suma}')
#     x=x+1
#     suma=suma+x

#
# x=0
# suma=0
# while suma<=100:
#     print(f'x={x} suma={suma}')
#     x+=1
#     suma+=x

#8. Napisz korzystajac z petli while program który wyświetli
#   10 kolejnych potęg liczby 2

#
# numer_potegi=0
# while numer_potegi<10:
#     numer_potegi+=1
#     print(numer_potegi,pow(2,numer_potegi))

#9. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość  potęgi
# nie przekroczy wartości podanej przez użytkownika


# max=int(input('daj maksymalna wartosc:\n'))
# p=0
# wp=0
# while wp<max:
#     print(p,wp)
#     p+=1
#     wp=pow(2,p)



#10. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
#od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od wartosci podanej przez uzytkownika
#
# import random
# print(random.random())
# print(random.randint(1,100))
#
# #x=random.randint(1,10)
#
# suma=0
# while suma<100:
#     print('dupa')
# import random
# max=int(input('podaj maksymalną wartość:\n'))
# suma=0
# while suma<max:
#     wylosowane=random.randint(1,10)
#     suma+=wylosowane
#     print(wylosowane,suma)

#przerwa obiadowa do 13:27

# tekst="siała BABA mak, nie wiedziała jak i dostała 10 lat bo nie płaciła VAT"
# print(tekst)
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.replace('a','X'))
# print(tekst.replace('a','X').replace('A',"X"))
# print(tekst.lower().replace('a','X'))
# print(len(tekst))
# lista=[1,2,3,4]
# print(len(lista))
# print("hajs "*10)
# if "BaBa".lower() in tekst.lower():
#     print('jest')
# else:
#     print('nie ma')
# print(tekst.title())
# print(tekst.count('a'))
# print(tekst.lower().count('a'))
# if "Java">"Python":
#     print('chyba śnisz')
# else:
#     print('no jaha')

#11. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z niego znaki ,.!?
# i wyświetli powiększony do dużych liter na konsoli

# tekst=input('podaj tekst:\n')
# print(tekst.replace('?','').replace('!','').replace('.','').replace(',','').upper())

# tekst=input('podaj tekst:\n')
# niechciane=['!','?','.',',']
# for n in niechciane:
#     tekst=tekst.replace(n,'')
# print(tekst)

#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia)


#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())

#12. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik