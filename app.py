from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe o corpo JSON da requisição
    req = request.get_json(force=True)

    print("\n===== JSON recebido =====")
    print(req)
    print("=========================\n")

    # Garante que os parâmetros existam
    if not req or "queryResult" not in req:
        return jsonify({"fulfillmentMessages": [{"text": {"text": ["Erro: requisição inválida."]}}]})

    parameters = req["queryResult"].get("parameters", {})
    nome = parameters.get("nome", "cliente")
    problema = parameters.get("problema", "problema não especificado")
    endereco = parameters.get("endereco", "endereço não informado")

    protocolo = random.randint(100, 999)

    fulfillment_text = f"{nome}, o chamado número {protocolo} foi aberto para o problema de {problema} no endereço {endereco}. Nossa equipe entrará em contato em breve!"

    response = {
        "fulfillmentMessages": [
            {"text": {"text": [fulfillment_text]}}
        ]
    }

    print("===== Resposta enviada =====")
    print(response)
    print("============================\n")

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
