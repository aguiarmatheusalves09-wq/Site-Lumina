from flask import Flask
from db import db
from models import Usuarios

usuario = "root"
senha_codificada = "123456"
host = "127.0.0.1"
porta = 3306
banco = "Lumina"

#connection_string = f"mysql+pymysql://{usuario}:{senha_codificada}@{host}:{porta}/{banco}"

app = Flask(__name__)

app.config['SQLALCHEMY_ENGINES'] = {"default": f"mysql+pymysql://{usuario}:{senha_codificada}@{host}:{porta}/{banco}"}

db.init_app(app) #inicializa o app com o banco de dados

from routes import * #Importa todas as coisas do arquivo rotas

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)






