# from flask import request, Flask
# from flask.json import jsonify
# from flask_restful import Api, Resource, abort
# from webargs import fields, validate
# from webargs.flaskparser import use_kwargs, parser
# from funcoes.funcoesKabum import procurarProdutosKabum
# from StockCheck import iniciar
# import decimal


# app = Flask(__name__)
# api = Api(app)

# limite = decimal.Decimal(13500.00)

# @app.route('/kabum')
# def query_example():
    
#     driver = iniciar()
#     disponiveisRsp = []
#     produto = request.args.get('produto')
    
#     produtoQuery = produto.replace(" ", "+")
    
#     url = 'www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=' + produtoQuery
#     adrs = "https://" + url
#     driver.get(adrs)
#     disponiveis = procurarProdutosKabum(driver, limite)
#     driver.quit()
#     return jsonify(nome=produto, url=url, disponiveis=str(len(disponiveis)))


# if __name__ == '__main__':
#     app.run(debug=True)