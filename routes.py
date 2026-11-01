#Rotas para as páginas

import os
from flask import render_template, request, url_for, redirect, session, jsonify
from sqlalchemy import or_
from werkzeug.utils import secure_filename
from datetime import date, timedelta
import re
from main import app
from db import db
from models import Usuarios

email_usuario = None  

app.secret_key = 'your_secret_key'  # Adicione uma chave secreta para a sessão

UPLOAD_FOLDER = os.path.join('static', 'uploads')
EXTENSOES_PERMITIDAS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'jfif'}

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False

def extensao_permitida(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in EXTENSOES_PERMITIDAS

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

        if not validar_email(email):
            return render_template('cadastro.html',
                                    css_path=css_,
                                    inicio_path=inicio_url,
                                    logo_path=logo_,
                                    login_path=login_url,
                                    erro_cadastro="Email inválido!")

        if db.session.query(Usuarios).filter(Usuarios.email == email).first():
            return render_template('cadastro.html',
                                   css_path=css_,
                                   inicio_path=inicio_url,
                                   logo_path=logo_,
                                   login_path=login_url,
                                   erro_cadastro="Usuário já cadastrado!")

        novo_usuario = Usuarios(
            email=email,
            senha=senha,  
            nome=nome,
            nickname=nickname,
            sequenciaDiaria=0,
            melhorSequencia=0,
            totalDiasAcesso=0,
            diasSemana="",
        )
        db.session.add(novo_usuario)
        db.session.commit()
        session['email_usuario'] = email  # Store email in session

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

        if usuario is not None and usuario.senha == login_senha:
            session['email_usuario'] = login_usuario  
            return redirect(url_for('principal_home')) 
        else:
            return render_template('login.html', 
                           css_path=css_,
                           inicio_path=inicio_url,
                           logo_path=logo_,
                           login_path=login_url,
                           cadastro_path=cadastro_url,
                           home_path=home_url,
                           erro_login="E-mail ou senha incorretos!")

    return redirect(url_for('home'))

@app.route("/home")
def principal_home():
    home_url = url_for('principal_home')
    rotina_url = url_for('rotina')
    materias_url = url_for('materias')
    desafios_url = url_for('desafios')
    sobre_url = url_for('sobre')
    config_url = url_for('configuracao')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    email_usuario = session.get('email_usuario')
    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()

    if not usuario:
        return redirect(url_for('home'))

    return render_template('home.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           rotina_path=rotina_url,
                           materias_path=materias_url,
                           desafios_path=desafios_url,
                           sobre_path=sobre_url,
                           config_path=config_url)

@app.route("/rotina")
def rotina():
    home_url = url_for('principal_home')
    config_url = url_for('configuracao')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    email_usuario = session.get('email_usuario')
    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()

    if usuario is None:
        return redirect(url_for('home'))

    return render_template('rotina.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           config_path=config_url,
                           email_usuario=email_usuario)

@app.route("/materias")
def materias():
    home_url = url_for('principal_home')
    config_url = url_for('configuracao')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    email_usuario = session.get('email_usuario')
    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()

    if usuario is None:
        return redirect(url_for('home'))

    return render_template('materias.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           config_path=config_url)

@app.route("/desafios")
def desafios():
    home_url = url_for('principal_home')
    config_url = url_for('configuracao')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    email_usuario = session.get('email_usuario')
    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()

    if usuario is None:
        return redirect(url_for('home'))

    return render_template('desafios.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           config_path=config_url)

@app.route("/sobre")
def sobre():
    home_url = url_for('principal_home')
    config_url = url_for('configuracao')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    email_usuario = session.get('email_usuario')
    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()

    if usuario is None:
        return redirect(url_for('home'))

    return render_template('sobre.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           config_path=config_url)

@app.route("/configuracao", methods=["GET", "POST"])
def configuracao():
    home_url = url_for('principal_home')

    logo_ = url_for('static', filename='imagens/logo.png')
    css_ = url_for('static', filename='style.css')

    email_usuario = session.get('email_usuario')
    if not email_usuario:
        return redirect(url_for('home'))

    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()
    if usuario is None:
        return redirect(url_for('home'))

    if request.method == "GET":
        dias_semana = usuario.diasSemana.split(",") if usuario.diasSemana else []
        return render_template('config.html', 
                           css_path=css_, 
                           logo_path=logo_,
                           home_path=home_url,
                           nome_usuario=usuario.nome,
                           nickname_usuario=usuario.nickname,
                           sequenciaDiaria=usuario.sequenciaDiaria or 0,
                           melhorSequencia=usuario.melhorSequencia or 0,
                           totalDiasAcesso=usuario.totalDiasAcesso or 0,
                           diasSemana=dias_semana,
                           foto_usuario=usuario.fotoPerfil,
                           email_usuario=usuario.email)

    elif request.method == "POST":
        novo_nome = request.form.get("nome")
        novo_nickname = request.form.get("nickname")
        novo_email = request.form.get("email")
        nova_senha = request.form.get("nova-senha")
        senha_atual = request.form.get("senha-atual")
        sequencia_diaria = request.form.get("sequenciaDiaria")
        foto = request.files.get("foto")

        print("DEBUG >> foto recebida no request.files:", foto)
        print("DEBUG >> nome do arquivo enviado:", foto.filename if foto else None)
        print("DEBUG >> senha_atual preenchida?", bool(senha_atual))

        dias_semana = usuario.diasSemana.split(",") if usuario.diasSemana else []
        dados_base = dict(
            css_path=css_,
            logo_path=logo_,
            home_path=home_url,
            nome_usuario=usuario.nome,
            nickname_usuario=usuario.nickname,
            sequenciaDiaria=usuario.sequenciaDiaria or 0,
            melhorSequencia=usuario.melhorSequencia or 0,
            totalDiasAcesso=usuario.totalDiasAcesso or 0,
            diasSemana=dias_semana,
            foto_usuario=usuario.fotoPerfil,
            email_usuario=usuario.email,
        )

        # confirma a senha atual antes de aceitar qualquer alteração
        if not senha_atual or senha_atual != usuario.senha:
            return render_template('config.html', **dados_base,
                                    erro_config="Senha atual incorreta!")

        if novo_nome:
            setattr(usuario, "nome", novo_nome)
        if novo_nickname:
            setattr(usuario, "nickname", novo_nickname)
        if novo_email and validar_email(novo_email):
            setattr(usuario, "email", novo_email)
        if nova_senha:
            setattr(usuario, "senha", nova_senha)

        if sequencia_diaria is not None:
            setattr(usuario, "sequenciaDiaria", int(sequencia_diaria))

        if foto and foto.filename and extensao_permitida(foto.filename):
            extensao = foto.filename.rsplit('.', 1)[1].lower()
            if extensao == 'jfif':
                extensao = 'jpg'
            email_seguro = secure_filename(usuario.email.replace("@", "_at_"))
            nome_arquivo = f"{email_seguro}.{extensao}"

            pasta_absoluta = os.path.join(app.root_path, UPLOAD_FOLDER)
            print("DEBUG >> pasta de upload:", pasta_absoluta)
            os.makedirs(pasta_absoluta, exist_ok=True)

            caminho_final = os.path.join(pasta_absoluta, nome_arquivo)
            foto.save(caminho_final)

            usuario.fotoPerfil = nome_arquivo

        db.session.commit()
        print("DEBUG >> commit feito. fotoPerfil no objeto após commit:", usuario.fotoPerfil)

        # a sessão guarda o e-mail como chave: se ele mudou, atualiza a sessão também
        session['email_usuario'] = usuario.email

        return redirect(url_for('configuracao'))


@app.route("/api/checkin", methods=["POST"])
def checkin():
    """Marca o acesso de hoje, calcula a sequência e grava tudo no banco."""
    email_usuario = session.get('email_usuario')
    if not email_usuario:
        return jsonify({"erro": "Não autenticado"}), 401

    usuario = db.session.query(Usuarios).filter(Usuarios.email == email_usuario).first()
    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    hoje = date.today()
    hoje_iso = hoje.isoformat()
    ontem_iso = (hoje - timedelta(days=1)).isoformat()

    # ultimoAcesso é String no banco, então comparamos como string (formato ISO: AAAA-MM-DD)

    # já marcou hoje: só devolve o estado atual
    if usuario.ultimoAcesso == hoje_iso:
        dias_semana = usuario.diasSemana.split(",") if usuario.diasSemana else []
        return jsonify({
            "jaMarcado": True,
            "sequenciaDiaria": usuario.sequenciaDiaria or 0,
            "melhorSequencia": usuario.melhorSequencia or 0,
            "totalDiasAcesso": usuario.totalDiasAcesso or 0,
            "diasSemana": dias_semana,
        })

    if usuario.ultimoAcesso == ontem_iso:
        usuario.sequenciaDiaria = (usuario.sequenciaDiaria or 0) + 1
    else:
        usuario.sequenciaDiaria = 1

    usuario.melhorSequencia = max(usuario.melhorSequencia or 0, usuario.sequenciaDiaria)
    usuario.totalDiasAcesso = (usuario.totalDiasAcesso or 0) + 1
    usuario.ultimoAcesso = hoje_iso

    dias_lista = usuario.diasSemana.split(",") if usuario.diasSemana else []
    if hoje_iso not in dias_lista:
        dias_lista.append(hoje_iso)

    cutoff_iso = (hoje - timedelta(days=6)).isoformat()
    dias_lista = [d for d in dias_lista if d and d >= cutoff_iso]
    usuario.diasSemana = ",".join(dias_lista)

    db.session.commit()

    return jsonify({
        "jaMarcado": False,
        "sequenciaDiaria": usuario.sequenciaDiaria,
        "melhorSequencia": usuario.melhorSequencia,
        "totalDiasAcesso": usuario.totalDiasAcesso,
        "diasSemana": dias_lista,
    })


#@app.route("/usuarios/<nome_usuario>")
#def usuarios(nome_usuario):
    #return render_template('usuarios.html', nome_usuario=nome_usuario)