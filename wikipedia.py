from flask import Flask, request, Response
from flask_restful import Resource, Api
import wikipediaapi

app = Flask(__name__)
api = Api(app)
wiki = wikipediaapi.Wikipedia('de')


class Status(Resource):
    def get(self):
        return 'WikipediaService is running'


class Answer(Resource):
    def post(self):
        page = wiki.page(request.data)
        if page.exists():
            message = '*{0}*\n{1}\n\n{2}'.format(page.title, page.summary, page.fullurl)
        else:
            message = "Leider konnte ich kein passendes Ergebnis finden. Bitte überprüfe, ob du dich vertippt hast."
        return Response(message, mimetype='application/json')


api.add_resource(Status, "/")
api.add_resource(Answer, "/api")

if __name__ == '__main__':
    app.run(port=8080, debug=True)
