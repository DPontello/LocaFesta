from flask import Flask
from flask_cors import CORS

# Importando os Blueprints dos controllers
from controllers.cliente_controller import clienteBp
from controllers.reserva_controller import reservaBp
from controllers.equipamento_controller import equipamentoBp

app = Flask(__name__)
CORS(app)

# Registrar os controllers com prefixo de rota
app.register_blueprint(clienteBp, url_prefix='/api')
app.register_blueprint(reservaBp, url_prefix='/api')
app.register_blueprint(equipamentoBp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
