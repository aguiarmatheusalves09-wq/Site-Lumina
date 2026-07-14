from flask import Flask

app = Flask(__name__)

from routes import * #Importa todas as coisas do arquivo rotas

#colocar o site no ar
if __name__ == "__main__": #vai rodar esse if se rodar o codigo nesse arquivo
    app.run(debug=True) #debug=True atualiza automaticamente as mudanças do site