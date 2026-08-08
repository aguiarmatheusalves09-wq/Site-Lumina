from flask import Flask
from db import db
from models import Usuarios

usuario = "root"
senha_codificada = "300303Porta#"
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
    #with app.app_context():

        #Base.metadata.create_all(db.engine)

        #user = Usuarios(email="peterlpk10@gmail.com", senha="123456", nome="Peter", data_nasc="10/10/2000", nickname="peterlpk")

        #db.session.add(user)

        #usuarios = db.session.query(Usuarios).all()
        #for usuario in usuarios:
            #print(usuario)

        #user = db.session.query(Usuarios).filter(Usuarios.email == "peterlpk10@gmail.com").first()
        #user.nome = "Henrique"
        #db.session.delete(user)
        #db.session.commit()

    app.run(debug=True)






