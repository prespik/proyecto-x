# app.py

from bottle import Bottle, run

app = Bottle()

@app.route('/')
def hello():
    return "¡Hola desde Bottle!"

# Importante: este host y puerto deben ser así para que Docker lo exponga
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)