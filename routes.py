#Rotas para as páginas
from flask import render_template, url_for
from main import app

@app.route("/")
def home():
    css_ = url_for('static', filename="style.css")
    return render_template('index.html', css_path=css_)

@app.route("/duvidas")
def duvidas():
    css_ = url_for('static', filename="style.css")
    return render_template('duvidas.html', css_path=css_)

@app.route("/sobre")
def sobre():
    css_ = url_for('static', filename="style.css")
    return render_template('sobre.html', css_path=css_)

@app.route("/funcionamento")
def funcionamento():
    css_ = url_for('static', filename="style.css")
    return render_template('funcionamento.html', css_path=css_)

@app.route("/cadastro")
def cadastro():
    css_ = url_for('static', filename="style.css")
    return render_template('cadastro.html', css_path=css_)