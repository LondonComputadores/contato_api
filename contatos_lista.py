from flask_restful import Resource

lista_contatos = ['Fulano', 'Cicrano', 'Beltrano', 'Gorfano']
class Contatos(Resource):
    def get(self):
        return lista_contatos