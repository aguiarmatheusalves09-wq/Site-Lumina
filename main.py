from flask import Flask, render_template

app = Flask(__name__)

from routes import * #Importa todas as coisas do arquivo rotas

if __name__ == "__main__":
    app.run()