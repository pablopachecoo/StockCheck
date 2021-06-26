from flask import request, Flask
from flask.json import jsonify
from flask_restful import Api, Resource, abort
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser

app = Flask(__name__)
api = Api(app)


@app.route('/')
def query_example():
    # if key doesn't exist, returns None
    produto = request.args.get('produto')
    produtoQuery = produto.replace(" ", "+")

    url = 'www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=' + produtoQuery
    return jsonify(produto, url)


# This error handler is necessary for usage with Flask-RESTful.
if __name__ == '__main__':
    app.run(debug=True)