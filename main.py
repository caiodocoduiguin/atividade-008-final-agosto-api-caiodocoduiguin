from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)


def chamada_api_professor(resultado):
    url = "https://apismsprofessor.menezesenderson.repl.co"
    headers = {"Authorization": os.environ["SENHA"]}
    dados_envio = {"numero": os.environ["NUMERO"], "mensagem": resultado}
    resposta = requests.post(url, headers=headers, json=dados_envio)
    return resposta

def create_app_flask():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return jsonify({"mensagem": "Hello, World!"})


    # ROTA PARA CONSULTA NO WIKIPEDIA

    # ROTA PARA CONSULTA API DO (EURO)

    # ROTA PARA CONVERSAO DE MOEDAS (EURO)

    # API QUE VOCES PODEM ESCOLHER

    return app

app = create_app_flask()
app.run(host="0.0.0.0", port=8080)
