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