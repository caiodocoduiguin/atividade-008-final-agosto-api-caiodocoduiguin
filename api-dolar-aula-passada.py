from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)


def chamada_api_professor(resultado):
    url = "https://apismsprofessor.menezesenderson.repl.co"
    headers = {"Authorization": os.environ["senha"]}
    dados_envio = {"numero": os.environ["zap"], "mensagem": resultado}
    resposta = requests.post(url, headers=headers, json=dados_envio)
    return resposta


@app.route("/")
def hello_world():
    real = request.args.get("real", None)
    if real:
        url = f"https://economia.awesomeapi.com.br/last/USD-BRL"
        texto_resposta = requests.get(url).json()
        valor_dolar = float(real) * float(texto_resposta["USDBRL"]["high"])
        valor_dolar = round(valor_dolar, 2)
        texto_resposta = f"O valor em real é {valor_dolar}"
        chamada_api = chamada_api_professor(texto_resposta)
        return jsonify(
            {"texto_enviado": texto_resposta, "chamada_api": chamada_api.json()}
        )
    else:
        return jsonify({"erro": "Precisa inserir real."})


app.run(host="0.0.0.0", port=8080)
