
from flask import Flask, request
from flask_restplus import Resource, Api, fields
from contatos_lista import Contatos
import json

app = Flask(__name__)
api = Api(app)

contatos = [
    {
        'id':'1',
        'nome':'Fulano',
        'canal':['fulano@email.com']
    },
    {
        'id':'2',
        'nome':'Cicrano',
        'canal':['cicrano@email.com']
    },
    {
        'id':'2',
        'nome':'Beltrano',
        'canal':['beltrano@email.com']
    }
]


# devolve um contato pelo ID, também altera e deleta um contato
class Contato(Resource):
    def get(self, id):
        try:
            response = contatos[id]
        except IndexError:
            mensagem = 'Contato de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        contatos[id] = dados
        return dados

    def delete(self, id):
        contatos.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
class ListaContatos(Resource):
    def get(self):
        return contatos

    def post(self):
        dados = json.loads(request.data)
        posicao = len(contatos)
        dados['id'] = posicao
        contatos.append(dados)
        return contatos[posicao]

api.add_resource(Contato, '/contato/<int:id>/')
api.add_resource(ListaContatos, '/contato/')
api.add_resource(Contatos, '/lista_contatos/')

if __name__ == '__main__':
    app.run(debug=True)