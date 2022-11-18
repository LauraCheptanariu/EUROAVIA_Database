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


@views.route('/', methods = ['GET', 'POST'])
def home():

    # atentiune aici, cand logam un viewer si cand logam un admin

    return render_template("home.html") # aici se face conexiunea cu front-end-ul

@views.route('/single_view', methods = ['GET', 'POST'])
def single_view():

    # aici for fi functionalitatile paginii

    return render_template("single_view.html")


@views.route('/multiple_view', methods = ['GET', 'POST'])
def multiple_view():

    # atentiune aici, cand cream un cont de viewer si cand cream un cont de admin

    return render_template("multiple_view.html")


@views.route('/admin', methods = ['GET', 'POST'])
def admin():

    # paginile de admin pot fi multiple (pe modelul aplicatiei de votare facute de mine)

    return render_template("admin.html")