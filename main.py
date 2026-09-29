from flask import Flask
from db import db

usuario = "root"
senha = ""
host = "127.0.0.1"
porta = 3306
banco = "Lumina"
#mysql://root:YYlpCCBdeJKeSUizJtJDxiEILSXekBVD@altaria.proxy.rlwy.net:58549/railway

#connection_string = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"

app = Flask(__name__)

app.config['SQLALCHEMY_ENGINES'] = {"default": f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"}

db.init_app(app) #inicializa o app com o banco de dados

from routes import * 

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
