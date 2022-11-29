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


# #
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())

#12. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik
#
# if len(linia.strip())>0:
# #
# plik=input('podaj nazwę pliku:\n')
# for linia in open(plik,encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(linia.strip())

#
# calosc=open('tadzio.txt',encoding='utf-8').read()
# print(calosc.upper())

#13. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego podanego przez użytkownika
# w pliku którego nazwę również poda użytkownik.

# plik=input('podaj nazwę pliku:\n')
# szukane=input('podaj szukaną frazę:\n')
# calosc=open(plik,encoding='utf-8').read().lower()
# ile=calosc.count(szukane.lower())
# print(f'ile={ile}')


# plik=input('podaj nazwę pliku:\n')
# szukane=input('podaj szukaną frazę:\n')
# ile=open(plik,encoding='utf-8').read().lower().count(szukane.lower())
# print(f'ile={ile}')


#
# x=open('tadzio.txt',encoding='utf-8').read().lower().count('a')
# print(x)

#14. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
 # poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
 #  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka po
 #    odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
 #  i  jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.
#
# if "baBa".lower() in "siała baba maK".lower():
#      print('jest')
# else:
#      print('nie ma')
#
# tekst='default'
# tekst=input('dupa:\n')


# plik=input('nazwa pliku:\n')
# szukane=input('szukane:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.lower() in linia.lower():
#         print(x,linia.strip())


# plik=input('nazwa pliku:\n')
# szukane=input('szukane:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.lower() in linia.lower().split():
#         print(x,linia.strip())


#przerwa do 14:52

# lista=[]
# lista=[1,2,3,'nietoperz','toperz']
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
# for element in lista:
#     print(element)

#15. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
#    Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
#
# lista=[]
# for x in range(1,11):
#     lista.append(pow(2,x))
#
# for e in lista:
#     print(e)

# lista=[1,2,3]
# print(lista)
# print(*lista)
#
# lista1=[1,2,3]
# lista2=[4,5,6]
# lista3=lista1+lista2
# print(lista3)
# print(*lista1,*lista2)
# lista3=[*lista1,*lista2]
# print(lista3)

# lista1=[1,2,3]
# lista2=[4,5,6]
# lista1.extend(lista2)
# print(lista1)

#
# lista1=[1,2,3]
# lista2=[4,5,6]
# lista3=[*lista1,*lista2]
# print(lista3)

#
# lista1=[1,2,3,4]
# print(lista1[3])
# print(lista1[0:3])

# lista1=[1,2,3,4]
# lista2=lista1
# lista1.clear()
# print(lista1)
# print(lista2)

# lista1=[1,2,3,4]
# lista2=lista1.copy()
# lista1.clear()
# print(lista1)
# print(lista2)


#16. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)

# print(lista.extend(inna))
# lista.extend(inna)
# print(lista)

# import random
# lista1=[]
# lista2=[]
# for x in range(10):
#     lista1.append(random.randint(1,10))
#     lista2.append(random.randint(1, 10))
# print(lista1)
# print(lista2)
# lista3=[*lista1,*lista2]
# print(lista3)
# lista4=lista1+lista2
# print(lista4)
# lista1.extend(lista2)
# print(lista1)

# import random
# lista1=[]
# lista2=[]
#
# for x in range(10):
#     lista1.append(random.randint(1,10))
#
# for x in range(10):
#     lista2.append(random.randint(1, 10))
#
# print(lista1)
# print(lista2)
# lista3=[*lista1,*lista2]
# print(lista3)
# lista4=lista1+lista2
# print(lista4)
# lista1.extend(lista2)
# print(lista1)
#
# lista=[
#     [1,'A'],
#     [2,'B'],
#     [3,'C']
# ]
#
# print(lista)
# for e in lista:
#     print(e)
#
# lista=[]
# for x in range(1,11):
#     podelement=[x,x*10]
#     lista.append(podelement)
#
# print(lista)

#
# lista=[]
# for x in range(1,11):
#     lista.append( [x,x*10] )
#
# print(lista)

#17. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.

# lista=[]
# x=0
# while True: #przepełnienie pamięci
#     x+=1
#     lista.append(x)
#
# lista=[]
# for x in range(1,11):
#     lista.append([x,pow(2,x)])
# print(lista)
# for e in lista:
#     print(e)
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11)]
# print(lista)
# print([x for x in range(1,11)])

# lista=[x*100 for x in range(1,11)]
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11) if x%2==0]
# print(lista)
#
# lista=[x*100 for x in range(1,11) if x%2==0]
# print(lista)
# 
# lista1=[1,2,3,4,5,6,7,8,9]
# lista2=[e*1000 for e in lista1 if e%2==0]
# print(lista2)
#
# lista=[ [e,e*1000] for e in range(1,11)]
# print(lista)

#18. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2

#
# lista=[pow(2,e) for e in range(1,11)]
# print(lista)
# print([pow(2,e) for e in range(1,11)])


#19. Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również będzie listą.
# Pierwszy element tej podlisty to numer potegi, a drugi to wartosc tej potegi dla liczby 2
#
# lista=[ [e,pow(2,e)] for e in range(1,11)]
# print(lista)
# for linia in open('dane.csv',encoding='utf-8'):
#     print(linia.strip())

#
# linia='1;Stefan;Burczymucha;1.76;80'
# lista=linia.split(';')
# print(lista[1])
# print(lista)
# print(lista[3]*2,type(lista[3]))
# print('1.76'*2)
# print(float(lista[3])*2)

#20. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska oraz wzrost i masę
#
# linia='1;a;b;c'
# print(type(linia))
# lista=linia.split(';')
# print(type(lista))
# d='dupa'
# print(sorted(d))
#
# linia='1;a;b;c'
# lista=linia.split(';')
# print(lista)
# csv=';'.join(lista)
# print(csv)

# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])


#
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().upper().split(';')
#     print(*lista[1:5])


#
# for linia in open('dane.csv',encoding='utf-8'):
#     print(*linia.strip().upper().split(';')[1:5])


#21. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv
# W w taki sposób   by linie oczyścic z bialych znaków i rozbić na listy.
# Każdy z elementów listy sam   powinien byc listą.
# Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy   linia po linii.

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     print(float(l[3])*10)

# for l in [e for e in open()]:
# #     print(l)






#przerwa do 10:19






#22. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
#    id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika
#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     wzrost=float(l[3])
#
#     print(l)

# print('tekst'+'tekst')
# print('tekst'+str(1))

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     w=float(l[3])
#     m=float(l[4])
#     bmi=round(m/pow(w,2),2)
#     print(l,bmi)

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     w=float(l[3])
#     m=float(l[4])
#     bmi=round(m/pow(w,2),2)
#     l.append(bmi)
#     print(l)

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     w=float(l[3])
#     m=float(l[4])
#     bmi=round(m/pow(w,2),2)
#     print(*l,bmi)

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     bmi=round(float(l[4])/pow(float(l[3]),2),2)
#     print(*l,bmi)

# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     bmi=round(float(l[4])/pow(float(l[3]),2),2)
#     print(*l,bmi)

#for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]: print(*l,round(float(l[4])/pow(float(l[3]),2),2))

# lista=[1,6,5,4,2,3,1]
# inna=sorted(lista)
# print(inna)
#lista.sort()
#lista.reverse()
# lista.sort(reverse=True)
# print(lista)
#
# lista=[1,6,5,4,2,3,1]
# inna=sorted(lista,reverse=True)
# print(inna)

#23. Wygeneruj listę 10 elementów o losowej wartości liczbowej, posortuj listę i wyświetl jej zawartość linia po linii

# import random
# lista=[]
# for x in range(10):
#     lista.append(random.randint(1,10))
#
# print(lista)
# lista.sort()
# for e in lista:
#     print(e)
#
# import random
# lista=[random.randint(1,10) for x in range(10)]
# lista.sort()
# print(lista)
# for e in lista:
#     print(e)

# lista=[
#     [1,"B"],
#     [3,'A'],
#     [2,'C']
# ]
# print(lista)
# lista.sort()
# print(lista)
#
# import operator
# lista=[
#     [1,"B"],
#     [3,'A'],
#     [2,'C']
# ]
# print(lista)
# lista.sort(key=operator.itemgetter(1))
# print(lista)

# class Osoba:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def __str__(self):
#         return str(self.__dict__)
#
# o1=Osoba('Andrzej','Klusiewicz')
# o2=Osoba('Twój','Stary')
# o3=Osoba('Chuck','Norris')
# lista=[o1,o2,o3]
# lista.sort(key=lambda x:x.last_name)
# for e in lista:
#     print(e)

# lista=[
#     [1,"B"],
#     [3,'A'],
#     [2,'C']
# ]
# lista.sort(key=lambda e:e[1])
# for e in lista:
#     print(e)

#24. Wczytaj do listy kolejne wiersze z pliku dane.csv. Dane posortuj po wzroscie i wyswietl linia po linii na konsoli.
#
# import operator
# wynik=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# wynik.sort(key=operator.itemgetter(3))
# for w in wynik:
#     print(w)
#
# wynik=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# wynik.sort(key=lambda e:e[3])
# for w in wynik:
#     print(w)
#
# def funkcja(e):
#     return e[3]

#
# wynik=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# wynik.sort(key=lambda e:float(e[3]))
# for w in wynik:
#     print(w)

#przerwa do 11:39

#25.  Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi
# wynik=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for w in wynik:
#     w.append(round(float(w[4])/pow(float(w[3]),2),2))
# wynik.sort(key=lambda e:e[5],reverse=True)
# for w in wynik:
#     print(w)

# lista=[1,4,1,2,3]
# lista.sort(reverse=True,key=lambda e:e)
#
# import operator
# wynik=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for w in wynik:
#     w.append(round(float(w[4])/pow(float(w[3]),2),2))
# wynik.sort(key=operator.itemgetter(5),reverse=True)
# for w in wynik:
#     print(w)
#
# tekst="siała baba mak"
# szukane='BAB'
# if szukane.lower() in tekst.lower():
#     print('jest')
# else:
#     print('nie ma')

# lista=['siała','baba','mak']
# szukane='ba'
# if szukane in lista:
#     print('jest')
# else:
#     print('nie ma')
#
# lista=['siała','baba','mak']
# szukane='ba'
# for e in lista:
#     if szukane.lower() in e.lower():
#         print(f'jest {szukane} w {e}')
#     else:
#         print(f'nie ma {szukane} w {e}')

#
# tekst="siała baba mak"
# print(tekst.count('a'))

# lista=[1,1,1,1,1,2,2,2,2,3,3,3,3]
# print(lista.count(1))
#
# import os
# for w in os.walk('e:\\'):
#     print(w)

#26.Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
# Wyszukiwarka ma być nieczuła na wielkość liter
#
#
# import os
# sciecha=os.path.join('e:\\','katalog','podkatalog')
# print(sciecha)

# import os
# for w in os.walk('e:\\'):
#     print(w)
