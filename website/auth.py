"""
1. Fisierul auth.py - cuprinde toate paginile ce tin de login/logout
2. Aveti mai jos exemplu de pagina - login
3. Pagini ce trebuie implementate:
    - login
    - logout
    - sign-up

* recomand sa va uitati la link ul de la pct 7 de pe main
"""

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():

    # aici for fi functionalitatile paginii

    return render_template("login.html") # aici se face conexiunea cu front-end-ul

@auth.route('/log_out', methods = ['GET', 'POST'])
def log_out():

    # aici for fi functionalitatile paginii

    return render_template("log_out.html")


@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():

    # aici for fi functionalitatile paginii

    return render_template("sign_up.html")