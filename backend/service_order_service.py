from flask import Flask, request, jsonify

app = Flask(__name__)
ORDERS = {}

@app.route('/criar_ordem', methods=['POST'])
def criar_ordem():
    data = request.json
    ordem_id = str(len(ORDERS) + 1)
    ORDERS[ordem_id] = {
        'cliente': data['cliente'],
        'descricao': data['descricao'],
        'status': 'PENDENTE'
    }
    return jsonify({'ordem_id': ordem_id})

@app.route('/atualizar_ordem', methods=['POST'])
def atualizar_ordem():
    data = request.json
    ordem_id = data['ordem_id']
    if ordem_id in ORDERS:
        ORDERS[ordem_id]['status'] = data['status']
        return jsonify({'status': 'Atualizado'})
    else:
        return jsonify({'erro': 'Ordem não encontrada'}), 404

@app.route('/listar_ordens', methods=['GET'])
def listar_ordens():
    return jsonify(ORDERS)

if __name__ == '__main__':
    app.run(port=5001)
