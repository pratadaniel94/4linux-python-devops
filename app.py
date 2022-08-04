from flask import Flask, jsonify
from pymongo import MongoClient

client = MongoClient(host='172.21.1.3', port=27017)
db = client['project_521']

app = Flask(__name__)


@app.route('/')
def hello_word():  # put application's code here
    db.usuario.insert_one({"name": "daniel"})
    return 'Hello World!'
@app.route('/usuarios')
def get_usuarios():
    return jsonify([{"_id": str(usuario['_id']), "name": usuario.get("name")} for usuario in db.usuario.find()])

@app.route('/usuarios/<name>')
def get_usuario(name):

    return jsonify([{"_id": str(usuario["_id"]), "name": usuario.get("name")} for usuario in db.usuario.find({"name": name})])

# desenvolvimento com branch





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)