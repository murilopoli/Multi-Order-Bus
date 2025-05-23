from flask import Flask, request, jsonify

app = Flask(__name__)
MESSAGES = []

@app.route('/notificar', methods=['POST'])
def notificar():
    data = request.json
    MESSAGES.append(data)
    return jsonify({'status': 'Notificação enviada'})

@app.route('/mensagens', methods=['GET'])
def mensagens():
    return jsonify(MESSAGES)

if __name__ == '__main__':
    app.run(port=5002)
