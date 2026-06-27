from flask import Flask

app = Flask(__name__)

@app.route('/')
def imprimir():
    return "Hola mundo usando venv y pip"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
