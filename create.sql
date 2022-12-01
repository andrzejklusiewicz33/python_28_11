create table testowa(x integer);
select * from testowa;


create table produkty (
	id_produktu serial primary key,
	nazwa text not null,
	cena numeric not null,
	opis text,
	stan integer default 0 not null
);

create table pracownicy(
id_pracownika serial primary key,
	imie text not null,
	nazwisko text not null,
	komentarz text
);

insert into produkty (nazwa,cena,opis,stan) values ('Bulbulator',100 ,'urzadzenie robiące bul bul',10);
insert into produkty (nazwa,cena,opis,stan) values ('Wihajster',20,'takie coś z takim czymś',100);

select * from produkty;

insert into pracownicy(imie,nazwisko,komentarz) values('Zenek','Martyniuk','...');
insert into pracownicy(imie,nazwisko,komentarz) values('Ferdynand','Kiepski','...');

select * from pracownicy;


create table zawodnicy(
	id_zawodnika integer primary key,
	imie text not null,
	nazwisko text not null,
	wzrost numeric not null,
	masa numeric not null
);