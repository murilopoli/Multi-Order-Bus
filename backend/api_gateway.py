from flask import Flask, request, jsonify
from backend import config
from backend.pubsub.redis_pubsub import RedisPubSub
from backend.pubsub.rabbitmq_pubsub import RabbitMQPubSub
from backend.pubsub.kafka_pubsub import KafkaPubSub

app = Flask(__name__)

# Middleware selection (in-memory, could be persisted)
current_middleware = config.DEFAULT_MIDDLEWARE

def get_pubsub():
    if current_middleware == 'redis':
        return RedisPubSub()
    elif current_middleware == 'rabbitmq':
        return RabbitMQPubSub()
    elif current_middleware == 'kafka':
        return KafkaPubSub()
    else:
        raise ValueError("Middleware inválido")

@app.route('/set_middleware', methods=['POST'])
def set_middleware():
    global current_middleware
    mw = request.json.get('middleware')
    if mw in config.MIDDLEWARES:
        current_middleware = mw
        return jsonify({'status': f'Middleware alterado para {mw}'})
    return jsonify({'error': 'Middleware inválido'}), 400

@app.route('/get_middleware', methods=['GET'])
def get_middleware():
    return jsonify({'middleware': current_middleware})

@app.route('/solicitar_manutencao', methods=['POST'])
def solicitar_manutencao():
    data = request.json
    msg = f"NOVA_SOLICITACAO|{data['cliente']}|{data['descricao']}"
    pubsub = get_pubsub()
    pubsub.publish('manutencao', msg)
    return jsonify({'status': f'Solicitação enviada via {current_middleware}'})

# Rotas para aprovar orçamento, finalizar serviço, etc. seguem o mesmo padrão

if __name__ == '__main__':
    app.run(port=5000)
