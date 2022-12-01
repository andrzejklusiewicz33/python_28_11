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
#
# import os
# szukane='oracle'
# for w in os.walk('e:\\'):
#     katalogi=w[1]
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print( os.path.join(w[0],k) )
#     pliki=w[2]
#     for p in pliki:
#         if szukane.lower() in p.lower():
#             print(os.path.join(w[0],p))


# import os
# szukane=input('czego szukasz:\n')
# start=input('podaj katalog startowy:\n')
# for w in os.walk(start):
#     for k in w[1]:
#         if szukane.lower() in k.lower():
#             print( os.path.join(w[0],k) )
#     for p in w[2]:
#         if szukane.lower() in p.lower():
#             print(os.path.join(w[0],p))


#PRZERWA OBIADOWA DO 13:29

# lista=[1,2,3]
# krotka=(5,6,1,2,3)
#print(sorted(krotka))

# lista=[1,2,3]
# krotka=(5,6,1,2,3)
# print(type(lista),type(krotka))


# lista=[1,2,3]
# krotka=tuple(lista)
# print(krotka,type(krotka))
# lista=list(krotka)
# print(lista,type(lista))
#
# krotka=(4,6,1,2,4)
# krotka=tuple(sorted(krotka))
# print(krotka)


# krotka=(4,6,1,2,4)
# lista=list(krotka)
# lista.sort()
# krotka=tuple(lista)
# print(krotka)
#
# krotka=(4,6,1,2,4)
# for e in krotka:
#     print(e)
#
# print('index 3:',krotka[3])
# print(krotka[0:4])

#27. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli
#trzecia=(*pierwsza,*druga)
# import random
# k1=tuple([random.randint(1,10) for e in range(10)])
# k2=tuple([random.randint(1,10) for e in range(10)])
# print(k1,type(k1))
# print(k2,type(k2))
# k3=(*k1,*k2)
# print(k3,type(k3))

#28. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
#
# lista=[tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# print(lista)
# for e in lista:
#     print(e)
#
# zbior={1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4}
# zbior.add(5)
# zbior.add(6)
# print(zbior)
# for z in zbior:
#     print(z)

# z1={1,2,3,4,5}
# z2={4,5,6,7,8}
# print('część wspólna: ',z1.intersection(z2))
# print('część wspólna: ',list(z1.intersection(z2)))
# print('suma zbiorów:',z1.union(z2))
# print('roznica z1-z2',z1-z2)
# print('roznica z2-z1',z2-z1)


#29. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną
# import random
# z1=set()
# z2=set()
# for x in range(20):
#     z1.add(random.randint(1,40))
#     z2.add(random.randint(1,40))
# print(z1)
# print(z2)
#
# z1=set([1,2,3,4])
# print(z1)

# import random
# z1={random.randint(1,40) for e in range(10)}
# print(z1,type(z1))

#import random
# z1=set()
# z2=set()
# for x in range(20):
#     z1.add(random.randint(1,40))
#     z2.add(random.randint(1,40))
# print(z1)
# print(z2)


# import random
# z1=set([random.randint(1,40) for e in range(20)])
# z2=set([random.randint(1,40) for e in range(20)])
# print(type(z1))


# import random
# z1={random.randint(1,40) for e in range(20)}
# z2={random.randint(1,40) for e in range(20)}
# print(z1)
# print(z2)
# print(z1.intersection(z2))
# print(z1.union(z2))
# print(z1.difference(z2))
# print(z2.difference(z1))

# l1=[
#     (1,'A'),
#     (2,'V'),
#     (1,'A')
# ]
# print(l1)
# z1=set(l1)
# print(z1)
#
# lista=[1,1,1,2,2,2,2,3,3,3]
# z1=set(lista)
# lista=list(z1)
# print(lista)

#30. Zduplikuj jeden z wierszy w pliku dane.csv. Napisz kod który zwróci do postaci
# listy krotek zawartość tego pliku z danymi bez powtórek.
#
# wynik=[tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# zestaw=set(wynik)
# wynik=list(zestaw)
# for w in wynik:
#     print(w)


# wynik=list(set([tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]))
# for w in wynik:
#     print(w)

#for w in list(set([tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')])): print(w)

#przerwa do 14:44
#
# sl=dict()
# sl['klucz1']='jakaś wartość'
# sl['inny_klucz']=1234
# sl['cos']=[1,2,3,4,5,6]
#
# print(sl['klucz1'])
#
# for key in sl:
#     print(key,sl[key])
#
# if 'klucz1' in sl:
#     print('mamy taki klucz')
# else:
#     print('nie mamy takiego klucza')

# #31. Stwórz plik ustawienia.txt i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości


# lista=[e.strip().split('=') for e in open('ustawienia.conf',encoding='utf-8')]
# sl=dict()
# for e in lista:
#     sl[e[0]]=e[1]
#
# for k in sl:
#     print(k,sl[k])
#
# print(sl['encoding'])

#32.Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone z nazwiskiem rozdzielone spacja,
# a pozostałe dane znalazły się w wartości
#   jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# sl=dict()
# for e in lista:
#     klucz=e[1]+' '+e[2]
#     wartosc=[e[0],e[3],e[4]]
#     sl[klucz]=wartosc
#
# for  k in sl:
#     print(k,sl[k])

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# sl=dict()
# for e in lista:
#     sl[e[1]+' '+e[2]]=[e[0],e[3],e[4]]
#
# for  k in sl:
#     print(k,sl[k])
# slowa=[]
# calosc=open('').read()

#33. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
# #
# lista=[
#     ("dupa",356),
#     ("dupa1",254),
#     ("dupa2",110)
# ]
# tekst='dupa !?,.....!!!! dupa'
# niechciane=['!','?','.',',']
# for n in niechciane:
#     tekst=tekst.replace(n,'')
# print(tekst)
#
# for x in range(85,120):
#     print(chr(x))

# Koza
# koza

# import time
# p=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['!','?','.',',',";",":",'/','(',')','…','-','«']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# sl=dict()
# for s in slowa:
#     if s in sl:
#         sl[s]+=1 #zwiększ wartość dla tego słowa o 1
#     else:
#         sl[s]=1 #dodaj wpis do słowanika o kluczu takim jak to słowo
# # for s in slowa: #fuuuuuuu
# #     print(s,slowa.count(s))
# for k in sl:
#     print(k,sl[k])
# #przepakowanie do listy krotek i posortowanie malejaco po liczbie wystapien
# # lista=[
# #     ("dupa",356),
# #     ("dupa1",254),
# #     ("dupa2",110)
# # ]
# k=time.time()
# print(f'trwało to :{k-p}s')

#
# slownik[s]=1
# slownik[s]=slownik[s]+1
# slownik[s]+=1

# if 'klucz' in slownik:
#     pass
#
#
# import time
# p=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['!','?','.',',',";",":",'/','(',')','…','-','«']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# sl=dict()
# for s in slowa:
#     if s not in sl:
#         sl[s]=1 #zwiększ wartość dla tego słowa o 1
#     else:
#         sl[s]+=1 #dodaj wpis do słowanika o kluczu takim jak to słowo
# # for s in slowa: #fuuuuuuu
# #     print(s,slowa.count(s))
# # wynik=[]
# # for k in sl:
# #     print(k,sl[k])
# #     krotka=(k,sl[k])
# #     wynik.append(krotka)
#
# wynik =[(k,sl[k]) for k in sl ]
# wynik.sort(key=lambda kr:kr[1],reverse=True)
# for w in wynik:
#     print(w)
# #przepakowanie do listy krotek i posortowanie malejaco po liczbie wystapien
# # lista=[
# #     ("dupa",356),
# #     ("dupa1",254),
# #     ("dupa2",110)
# # ]
# k=time.time()
# print(f'trwało to :{k-p}s')



#
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# for n in ['!','?','.',',',";",":",'/','(',')','…','-','«']: calosc=calosc.replace(n,'')
# sl=dict()
# for s in calosc.split():
#     if s not in sl:
#         sl[s]=1
#     else:
#         sl[s]+=1
# wynik =[(k,sl[k]) for k in sl ]
# wynik.sort(key=lambda kr:kr[1],reverse=True)
# for w in wynik: print(w)

#matplotlib / seaborn


#przerwa do 10:16

# import pakiecik.modul as pm
# pm.dupa()

# import random
# import matplotlib.pyplot as plt
# lista1=[random.randint(1,100) for e in range(10)]
# lista2=[random.randint(-100,100) for e in range(10)]
# plt.plot(lista1,'#FF0000',label="czerwona kreska")
# plt.plot(lista2,"#00FF00",label="zielona kreska")
# plt.xlabel("wartości osi X")
# plt.ylabel("funkcja od X")
# plt.grid()
# plt.legend()
# plt.savefig('wykres.png')
# plt.show()
# import random
# import matplotlib.pyplot as plt
# wartosci=[random.randint(1,100) for e in range(10)]
# osx=[e for e in range(1,11)]
# plt.bar(osx,wartosci)
# plt.show()

# import random
# import matplotlib.pyplot as plt
# lista=[pow(2,x) for x in range(1,11)]
# plt.plot(lista,'r--')
# # wartosci=[random.randint(1,1000) for e in range(10)]
# # osx=[e for e in range(1,11)]
# # plt.bar(osx,wartosci)
# #plt.grid()
# plt.show()

#34. Stwórz program ktory przez zmienne przyjmie kwotę, ilość lat i wysokość inflacji,
# a następnie na wykresie przedstawi spadek wartości nabywczej podanej kwoty na przestrzeni lat.

# import matplotlib.pyplot as plt
# kwota=100000
# inflacja=-0.2
# ilosc_lat=5
# dane=[kwota]
# for r in range(1,ilosc_lat+1):
#     kwota=round(kwota+(kwota*inflacja))
#     dane.append(kwota)
# print(dane)
# plt.plot(dane,'#FF0000',label=f"wartość {kwota} na przestrzeni {ilosc_lat} lat")
# plt.legend()
# plt.grid()
# plt.show()
# osx=[e for e in range(1,11)]
# plt.plot(osx,dane)

# import matplotlib.pyplot as plt
# plt.plot([pow(2,x) for x in range(1,11)])
# plt.show()
# import matplotlib.pyplot as plt
# lista=[pow(2,x) for x in range(1,11)]
# plt.plot(lista)
# plt.show()

#35. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.

# for x in range(-10,11):
#     print(x,1/x)

# try:
#     print(1/0)
# except:
#     print('kupa!')
# print('coś dalej')

#
# try:
#     print(1/0)
# except Exception as e:
#     print(f'error={e}')
# print('coś dalej')



# try:
# #    raise IndexError
#     print(1/0)
# except IndexError:
#     print('to się nie ma prawa zdarzyć')
# except ZeroDivisionError:
#     print('dzielić przez zero potrafi tylko Chuck Norris')
# except Exception as e:
#     print(f'error={e} type(e)={type(e)}')
# print('coś dalej')


#raise Exception('kij ci w oko!')

#36. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10 w taki sposob by
# w przypadku wyjatku nie przerywac dzialania petli a po prostu wyswietlic na konsoli informację
# o błędzie i przejsc do dalszego przetwarzania

# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'dzielenie przez zero na x={x}')

# try: #fuuuuuuu
#     for x in range(-10,11):
#         print(1/x)
# except ZeroDivisionError:
#     print('muka')

#przerwa do 11:46

#37. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
# Nie podmieniaj przecinków etc w tekscie. W przypadku pojawienia się wyjątku na obliczaniu bmi dla
# któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;IOERROR
#
# plik=open('output.txt',encoding='utf-8',mode='a')
# for x in range(1,11):
#     plik.write(f'element numer {x}\n')

# linia='1;Andrzej;Klusiewicz;1.76;80'
# lista=linia.split(';')
# print(lista)
# nowa_linia=";".join(lista)+"\n"
# print(nowa_linia)
#
# lista=[linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# for e in lista:
#     try:
#         bmi=round(float(e[4])/pow(float(e[3]),2),2)
#         print(e,bmi)
#     except ValueError:
#         plik=open('errors.csv',encoding='utf-8',mode='a')
#         linia=';'.join(e)+";ValueError\n"
#         plik.write(linia)

#
# for e in [linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     try:
#         print(e,round(float(e[4])/pow(float(e[3]),2),2))
#     except ValueError:
#         open('errors.csv',encoding='utf-8',mode='a').write(';'.join(e)+";ValueError\n")

#tkinter

# def hello():
#     print('Hiszpańska Inkwizycja')
#
# hello()

# def hello(imie):
#     print(f'Hello {imie}')
#
# hello('Andrzej')
#
# def hello(imie,nazwisko):
#     print(f'Hello {imie} {nazwisko}')
#
# hello('Andrzej','Klusiewicz')
#
# def mnozenie(x,y):
#     # wynik=x*y
#     # return wynik
#     return x*y
#
# wynik=mnozenie(6,9)
# print(wynik)
# print(mnozenie(5,6))

#38. Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.

# def bmi(w,m):
#     try:
#         return round(m/pow(w,2),2)
#     except:
#         pass
#         return -1
#
# wzrost=0#1.76
# masa=80
# wynik=bmi(wzrost,masa)
# print(wynik)
#
# def wtf():
#     return 1,2
#
# a,b=wtf()
# print(a)
# print(b)


# def bmi(w,m):
#     try:
#         #raise IndentationError
#         return round(m/pow(w,2),2)
#     except ZeroDivisionError:
#         print('podany wzrost wynosi 0')
#         return -1
#     except TypeError:
#         print(f'podałeś coś innego niż liczbę type(w)={type(w)} type(m)={type(m)}')
#         return -1
#     except Exception as e:
#         print(f'jakiś inny wyjątek e={e} type(e)={type(e)}')
#
# wzrost='dupa'#0#1.76
# masa=80
# wynik=bmi(wzrost,masa)
# print(wynik)

# import time
# def mierzczas(fun):
#     def wewnetrzna(*args,**kwargs):
#         p=time.time()
#         print('dekorator!')
#         fun(*args,**kwargs)
#         k=time.time()
#         print(f'funkcja {fun.__name__} trwała {k-p}s')
#     return wewnetrzna
#
# @mierzczas
# def funkcja():
#     time.sleep(2)
#     print('funkcja!')
#
# funkcja()

# f=mierzczas(funkcja)
# f()

#PRZERWA OBIADOWA DO 13:35

#
# def funkcja(a,b):
#     pass
#
# funkcja(1,2)

# def witacz(imie,nazwisko,wiek='nie podano'):
#     print(f'witaj {imie} {nazwisko} masz {wiek} lat')
#
# witacz('Andrzej','Klusiewicz',36)
# witacz('Andrzej','Klusiewicz')


# def witacz(imie,nazwisko,wiek='nie podano'):
#     print(f'witaj {imie} {nazwisko} masz {wiek} lat')
#
# witacz('Andrzej','Klusiewicz',36)
# witacz('Andrzej','Klusiewicz')

#39.  Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku CSV
  # którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
  # podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie pdane ma przyjac utf-8
  #Rozszerzenie - rodzielacz kolumn niech też będzie konfigurowalny przy wywołaniu funkcji

# def list_me(file_name,enc='utf-8',divider=';'):
#     return [tuple(e.strip().split(divider)) for e in open(file_name, encoding=enc)]
#
# #wynik=list_me('dane.csv','utf-8',';')
# #wynik=list_me('dane.csv',divider=' ')
# for w in wynik:
#     print(w)
#
# for w in list_me('dane.csv'):
#     print(w)
#
# def list_me(file_name,enc='utf-8',divider=';'):
#     return [tuple(e.strip().split(divider)) for e in open(file_name, encoding=enc)]


#
# en=input('podaj_kodowanie:\n')
# if len(en.strip())==0:
#     en='jakas wartosc'

#
#40. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.

#
# def list_me(file_name,enc='utf-8',divider=';'):
#     return [tuple(e.strip().split(divider)) for e in open(file_name, encoding=enc)]
#
# def print_me(result):
#     for r in result:
#         print(r)
#
# wynik=list_me('dane.csv')
# print_me(wynik)
#
# print_me( list_me('dane.csv') )
#
# import moj_modul
# moj_modul.siemator()


# import moj_modul as mm
# mm.siemator()
#
# from moj_modul import siemator
# siemator()
#
# from invoice_dao import * #fuuuuu
# from participants_dao import * #fuuuuu
# print(get_all())

# import invoice_dao as idao
# import participants_dao as pdao
# print(idao.get_all())
# print(pdao.get_all())

#import invoice_dao

#import this

# import dao.invoice_dao
# print(dao.invoice_dao.get_all())

#
# import dao.invoice_dao as idao
# print(idao.get_all())

from dao.invoice_dao import  * #fuuuuuu
#print(get_all())

#41.Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.

# for e in open('dane\\dane.csv',encoding='utf-8'):
#     print(e.strip())
#
# import body.functions
# print(body.functions.bmi(1.7,90))
#
# import body.functions as bf
# print(bf.bmi(1.7,90))
#
# from body.functions import *
# print(bmi(1.7,90))
# #
# import matplotlib.pyplot as plt
# plt.plot()

#przerwa do 14:57

#PostgreSQL

# class Osoba:
#     imie='Andrzej'
#     nazwisko='Klusiewicz'
#     lista=[]
#     def __str__(self):
#         #return "dupa"
#         return str(self.__dict__)
#
# o=Osoba()
# print(o.__dict__)
#
# import requests as re
# response=re.get('https://jsystems.pl/static/blog/python/dane.json')
# print(response.status_code)
# if response.status_code==200:
#     dane=response.json()
#     print(dane)


#
# import requests as re
# response=re.get('https://jsystems.pl/static/blog/python/dane.json')
# print(response.status_code)
# if response.status_code==200:
#     dane=response.json()
#     print(dane['nazwisko'])
#     adres=dane['adres']
#     print(adres['miasto'])
#     print(dane['adres']['miasto'])
#     jezyki=dane['jezyki']
#     for j in jezyki:
#         print(j)
#     for e in dane['jezyki']:
#         print(e)
#

#42. z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do pobierz informację o szkoleniach.
# na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają malymi badz duzymi
# literami "Java" lub "JavaScript" i status terminu gwarantowanego (pole terminyGwarantowany=1)

#BeautifulSoup


#
# import requests
# response=requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code==200:
#     dane=response.json()
#     for s in dane:
#         if 'java' in s['tytul_szkolenia'].lower() and s['terminyGwarantowany']==1:
#             print(s['tytul_szkolenia'],s['termin'],s['miasto'])
#


#
# import requests
# response=requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code==200:
#     for e in [s for s in response.json() if 'java' in s['tytul_szkolenia'].lower() and s['terminyGwarantowany']==1]:
#         print(e['tytul_szkolenia'], e['termin'], e['miasto'])


#dbeaver

#przerwa do 10:35

#13.74.139.54
#szkolenie_jsystems_2021

import psycopg2 #PSYCOPG2
connection=psycopg2.connect(host="localhost",database="andrzej",user="andrzej", password="oracle", port=5432)