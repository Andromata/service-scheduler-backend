from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde tu primer backend en Python!'

if __name__ == '__main__':
    app.run(debug=True)
