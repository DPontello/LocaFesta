from flask import Flask
from flask_cors import CORS

# Importando os Blueprints dos controllers
from controllers.cliente_controller import cliente_bp
from controllers.reserva_controller import reserva_bp
from controllers.equipamento_controller import equipamento_bp

app = Flask(__name__)
CORS(app)

# Registrar os controllers com prefixo de rota
app.register_blueprint(cliente_bp, url_prefix='/api')
app.register_blueprint(reserva_bp, url_prefix='/api')
app.register_blueprint(equipamento_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
