#Rotas para as páginas
from flask import render_template, request, url_for, redirect
from sqlalchemy import or_
from main import app
from db import db
from models import Usuarios

@app.route("/")
def home():
    duvidas_url = url_for('duvidas')
    sobre_url = url_for('sobre')
    funcionamento_url = url_for('funcionamento')
    cadastro_url = url_for('cadastro')
    conecte_url = url_for('conecte')

    logo_ = url_for('static', filename='imagens/logo.png')
    estudante_ = url_for('static', filename='imagens/estudante.jpg')
    css_ = url_for('static', filename='style.css')

    return render_template('index.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           estudante_path=estudante_, 
                           duvidas_path=duvidas_url, 
                           sobre_path=sobre_url,
                           funcionamento_path=funcionamento_url,
                           cadastro_path=cadastro_url,
                           conecte_path=conecte_url)

@app.route("/duvidas")
def duvidas():
    inicio_url = url_for('home') #home -> função
    sobre_url = url_for('sobre') #sobre -> função
    funcionamento_url = url_for('funcionamento') #funcionamento -> função
    conecte_url = url_for('conecte')

    logo_ = url_for('static', filename='imagens/logolumina.png')
    nagi_ = url_for('static', filename='imagens/nagicelula.png')
    reo_ = url_for('static', filename='imagens/reoteste.png')
    css_ = url_for('static', filename='style.css')

    return render_template('duvidas.html',
                            css_path=css_,
                            logo_path=logo_,
                            nagi_path=nagi_,
                            reo_path=reo_,
                            inicio_path=inicio_url,
                            sobre_path=sobre_url,
                            funcionamento_path=funcionamento_url,
                            conecte_path=conecte_url)

@app.route("/sobre")
def sobre():
    inicio_url = url_for('home') 
    duvidas_url = url_for('duvidas')
    funcionamento_url = url_for('funcionamento')
    conecte_url = url_for('conecte')

    logo_ = url_for('static', filename='imagens/logolumina.png')
    rin_ = url_for('static', filename='imagens/rinsobree.png')
    css_ = url_for('static', filename='style.css')

    return render_template('sobre.html', 
                           css_path=css_,
                           logo_path=logo_, 
                           rin_path=rin_,
                           inicio_path=inicio_url, 
                           funcionamento_path=funcionamento_url, 
                           duvidas_path=duvidas_url,
                           conecte_path=conecte_url)

@app.route("/funcionamento")
def funcionamento():
    inicio_url = url_for('home') 
    duvidas_url = url_for('duvidas')
    sobre_url = url_for('sobre')
    conecte_url = url_for('conecte')

    logo_ = url_for('static', filename='imagens/logolumina.png')
    sae_ = url_for('static', filename='imagens/saelegal.png')
    css_ = url_for('static', filename='style.css')

    return render_template('funcionamento.html', 
                           css_path=css_,
                           logo_path=logo_, 
                           sae_path=sae_, 
                           inicio_path=inicio_url, 
                           sobre_path=sobre_url, 
                           duvidas_path=duvidas_url,
                           conecte_path=conecte_url)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    inicio_url = url_for('home') 
    duvidas_url = url_for('duvidas')
    sobre_url = url_for('sobre')
    funcionamento_url = url_for('funcionamento')
    conecte_url = url_for('conecte')

    css_ = url_for('static', filename='style.css')
    logo_ = url_for('static', filename='imagens/logolumina.png')


    if request.method == "GET":
        return render_template('cadastro.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           duvidas_path=duvidas_url,
                           sobre_path=sobre_url,
                           funcionamento_path=funcionamento_url,
                           logo_path=logo_,
                           conecte_path=conecte_url)
    elif request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        nickname = request.form.get("nickname")
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        ano = request.form.get("ano")

        novo_usuario = Usuarios(email=email, senha=senha, nome=nome, data_nasc=f"{ano}-{mes}-{dia}", nickname=nickname)
        if db.session.query(Usuarios).filter(or_(Usuarios.email == email, Usuarios.nickname == nickname)).first():
            return render_template('cadastro.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           duvidas_path=duvidas_url,
                           sobre_path=sobre_url,
                           funcionamento_path=funcionamento_url,
                           logo_path=logo_,
                           conecte_path=conecte_url,
                           erro_cadastro="Usuário já cadastrado!")
        else:
            db.session.add(novo_usuario)
            db.session.commit()

            return redirect(url_for('home'))
        
@app.route("/conecte-se", methods=["GET", "POST"])
def conecte():
    inicio_url = url_for('home') 
    duvidas_url = url_for('duvidas')
    sobre_url = url_for('sobre')
    funcionamento_url = url_for('funcionamento')
    conecte_url = url_for('conecte')
    cadastro_url = url_for('cadastro')

    css_ = url_for('static', filename='style.css')
    logo_ = url_for('static', filename='imagens/logolumina.png')

    if request.method == "GET":
        return render_template('conecte.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           duvidas_path=duvidas_url,
                           sobre_path=sobre_url,
                           funcionamento_path=funcionamento_url,
                           logo_path=logo_,
                           conecte_path=conecte_url,
                           cadastro_path=cadastro_url)

    elif request.method == "POST":
        login_usuario = request.form.get("login-usuario")
        login_senha = request.form.get("login-senha")

        usuario = db.session.query(Usuarios).filter(or_(Usuarios.email == login_usuario, Usuarios.nickname == login_usuario)).first()

        if usuario and usuario.senha == login_senha:
            return redirect(url_for('home')) 
        else:
            return render_template('conecte.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           duvidas_path=duvidas_url,
                           sobre_path=sobre_url,
                           funcionamento_path=funcionamento_url,
                           logo_path=logo_,
                           conecte_path=conecte_url,
                           cadastro_path=cadastro_url,
                           erro_login="Email ou senha incorretos!")


#@app.route("/usuarios/<nome_usuario>")
#def usuarios(nome_usuario):
    #return render_template('usuarios.html', nome_usuario=nome_usuario)