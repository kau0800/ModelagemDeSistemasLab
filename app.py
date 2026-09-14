```python
from flask import Flask, request, jsonify, render_template
from frete import calcular_frete

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json() or {}
    valor_carrinho = data.get('valor_carrinho')
    regiao = data.get('regiao')

    try:
        resultado = calcular_frete(valor_carrinho, regiao)

        if isinstance(resultado, tuple):
            frete, status = resultado
            return jsonify({'frete': frete, 'status': status}), 200
        elif isinstance(resultado, dict):
            return jsonify(resultado), 200

        return jsonify({'frete': resultado, 'status': 'Calculado'}), 200

    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro interno no servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True)
```