from flask import Flask, make_response, jsonify, request
from db_alunos import Alunos


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/alunos', methods=['GET'])
def get_alunos():
    return make_response(
        jsonify(
            message ='Lista de alunos.',
            Alunos = Alunos
        )
    )

@app.route('/alunos', methods=['POST'])
def add_alunos():
    alunos = request.json
    Alunos.append(alunos)
    return make_response(
        jsonify(
            message='Aluno cadastrados com sucesso.',
            alunos = alunos
        )
    )
        

app.run()