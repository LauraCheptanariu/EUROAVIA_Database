"""
1. Fisierul model.py al programului -  aici dam forma bazei de date ce sta in spatele web app-ului
2.  Avand in vedere ca lucram cu SQLAlchemy, informatia pe care o punem in aceasta baza de date
trebuie sa fie una tabelata. Asa ca, pentru a intelege ce se intampla mai jos, trebuie sa va imaginati un tabel
numit Person, ce are urmatoarele coloane: id, name, department. 
3. Ce facem aici nu este sa cream tabelul, ci mai degraba sa cream matrita (capul de tabel) pe care vom lucra
4. De modificat: 
    - trebuie sa primim de la dept Legal un tabel cu toate info despre persoane si vom adauga aici 
    atributele (coloanele) respective (class Person)
    - class Admin (conturile pentru admini - ei pot sa editeze info)
    - class Viewer (conturile pentru cei care pot sa vada info, dar nu sa le editeze)

** formatul unei coloane este de genul: x = db.Column(db.String(nr maxim de caractere)) sau 
 x = db.Column(db.Integer); acestea sunt cele mai comune. Pentru mai multe info, consultati doc SQLAlchemy
"""

from . import db 


class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True) #toate clasele pe care le cream aici incep cu id
    name = db.Column(db.String(150))
    department = db.Column(db.String(150))

    """
    metoda __init__ da niste valori standard obiectelor pe care le cream in cazul in care acestea nu sunt pasate de catre noi

    """

    def __init__(self, name= 'Nume', departament= 'niciunul'): 
        self.name = name                                      
        self.departament = departament


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True) #toate clasele pe care le cream aici incep cu id


class Viewer(db.Model):
    id = db.Column(db.Integer, primary_key = True) #toate clasele pe care le cream aici incep cu id
