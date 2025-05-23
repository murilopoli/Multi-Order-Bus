# Service Bus Solution

## Visão Geral

Solução de mensageria orientada a eventos para integração entre clientes, técnicos e serviços de backend, com suporte dinâmico a Redis, RabbitMQ e Kafka como barramento de comunicação. Permite alternar o middleware tanto via interface gráfica quanto por configuração.

## Arquitetura

- **Frontend:** Interface web para cliente e técnico, seleção dinâmica do middleware.
- **API Gateway:** Recebe requisições HTTP e publica mensagens no barramento selecionado.
- **Serviços Backend:** Messaging Service e Service Order Service, consumindo eventos do barramento.
- **Barramento de Comunicação:** Redis, RabbitMQ ou Kafka, selecionável em tempo real.

## Instalação

1. Instale Redis, RabbitMQ e/ou Kafka conforme desejado.
2. Clone o repositório e instale as dependências:
cd backend
pip install -r requirements.txt
3. Inicie os serviços backend:
python api_gateway.py
python messaging_service.py
python service_order_service.py
4. Inicie o frontend:
cd frontend
python app.py
5. Acesse `http://localhost:8080` para o cliente e `/tecnico` para o técnico.

## Configuração

- O middleware padrão pode ser definido via variável de ambiente `MIDDLEWARE` ou alterado em tempo real via interface gráfica.
- Configure os hosts e portas dos brokers em `backend/config.py` ou via variáveis de ambiente.

## Funcionalidades

- Solicitação, aprovação e finalização de serviços via eventos pub/sub.
- Seleção dinâmica do barramento de comunicação.
- Visualização e gerenciamento de ordens e notificações.

## Referências

- Diagramas de arquitetura, BPMN e sequência anexados.
- [DZone: Integrating Redis with Message Brokers][5]
- [Logit.io: RabbitMQ vs Kafka vs Redis][12]

---
