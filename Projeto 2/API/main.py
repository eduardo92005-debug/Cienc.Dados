from flask import Flask, jsonify, request
import json
import requests
app = Flask('a')

def auxregistro(data):
    return data

@app.route("/index", methods=["GET"])
def index():
    return {"Rodando na porta":"5050"}

@app.route("/registros", methods=["POST"])
def registros():
    data = request.get_json()
    dataset = {
        "Email": "carlos",
    }
    return jsonify(dataset)


@app.route("/seleciona/usuario")
def selecionaUsuario(email):
    return email
@app.route("/seleciona/usuario/<string:email>/<string:filme>&token=<int:mytoken>", methods=["GET"])
def selecionaFilme(email, filme,mytoken):
    objJson = [
        {"Email": email},
        {"Filme": filme}
    ]

    return json.dumps(objJson)

app.run(host="localhost", port=5095)
