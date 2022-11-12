"""
1. Fisierul views.py - cuprinde toate paginile mai putine cele de logare/delogare
2. Aveti mai jos un exemplu de pagina -  home 
3. Pagini ce trebuie implementate:
     - home
     - person_view: pagina pe care se vor afisa informatiile despre persoana ceruta 
        * aici sa tinem cont ca in functie de statutul cu care te loghezi poti vedea unele info sau pe toate
     - (lasam pe mai incolo) statistic_view: o pagina pe care vom afisa statistici despre persoane (exemplu - cate persoane sunt anul 1)
     - attendance (o pagina in care heads vor face prezenta la sedinta)
     - admin: de aici poti adauga/sterge/modifica info despre persoane

*trebuie sa tinem cont ce pagini au nevoie de @login.required si care nu au nevoie
"""

from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/login', methods = ['GET', 'POST'])
def login():

    # aici for fi functionalitatile paginii

    return render_template("login.html") # aici se face conexiunea cu front-end-ul


