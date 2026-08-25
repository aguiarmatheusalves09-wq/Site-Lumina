#Rotas para as páginas
from flask import render_template, request, url_for, redirect
from sqlalchemy import or_
import re
from main import app
from db import db
from models import Usuarios

@app.route("/")
def home():
    cadastro_url = url_for('cadastro')
    login_url = url_for('login')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('index.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           cadastro_path=cadastro_url,
                           login_path=login_url)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    inicio_url = url_for('home') 
    login_url = url_for('login')

    css_ = url_for('static', filename='style.css')
    logo_ = url_for('static', filename='imagens/logo.png')


    if request.method == "GET":
        return render_template('cadastro.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           logo_path=logo_,
                           login_path=login_url)
    elif request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        nickname = request.form.get("nickname")

        novo_usuario = Usuarios(email=email, senha=senha, nome=nome, nickname=nickname)
        def validar_email(email):
            padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(padrao, email):
                return True
            return False 

        if not validar_email(email):
            return render_template('cadastro.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           logo_path=logo_,
                           login_path=login_url,
                           erro_email="Email inválido!")

        elif db.session.query(Usuarios).filter(Usuarios.email == email).first():
            return render_template('cadastro.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           logo_path=logo_,
                           login_path=login_url,
                           erro_cadastro="Usuário já cadastrado!")

        else:
            db.session.add(novo_usuario)
            db.session.commit()

            return redirect(url_for('principal_home'))
        
@app.route("/login", methods=["GET", "POST"])
def login():
    inicio_url = url_for('home') 
    login_url = url_for('login')
    cadastro_url = url_for('cadastro')
    home_url = url_for('principal_home')


    css_ = url_for('static', filename='style.css')
    logo_ = url_for('static', filename='imagens/logo.png')

    if request.method == "GET":
        return render_template('login.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           logo_path=logo_,
                           login_path=login_url,
                           cadastro_path=cadastro_url,
                           home_path=home_url)

    elif request.method == "POST":
        login_usuario = request.form.get("email")
        login_senha = request.form.get("senha")

        usuario = db.session.query(Usuarios).filter(Usuarios.email == login_usuario).first()

        if usuario and usuario.senha == login_senha:
            return redirect(url_for('principal_home')) 
        else:
            return render_template('login.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           logo_path=logo_,
                           login_path=login_url,
                           cadastro_path=cadastro_url,
                            home_path=home_url,
                           erro_login="Email ou senha incorretos!")

@app.route("/home")
def principal_home():
    home_url = url_for('principal_home')
    rotina_url = url_for('rotina')
    materias_url = url_for('materias')
    desafios_url = url_for('desafios')
    sobre_url = url_for('sobre')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('home.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           rotina_path=rotina_url,
                           materias_path=materias_url,
                           desafios_path=desafios_url,
                           sobre_path=sobre_url)

@app.route("/rotina")
def rotina():
    home_url = url_for('principal_home')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('rotina.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url)

@app.route("/materias")
def materias():
    home_url = url_for('principal_home')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('materias.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url)

@app.route("/desafios")
def desafios():
    home_url = url_for('principal_home')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('desafios.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url)

@app.route("/sobre")
def sobre():
    home_url = url_for('principal_home')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('sobre.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url)

@app.route("/configuracao")
def configuracao():
    home_url = url_for('principal_home')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    return render_template('config.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url)


#@app.route("/usuarios/<nome_usuario>")
#def usuarios(nome_usuario):
    #return render_template('usuarios.html', nome_usuario=nome_usuario)