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