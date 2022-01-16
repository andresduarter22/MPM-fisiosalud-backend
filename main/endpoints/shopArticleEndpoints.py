"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.shop_article import ShopArticle


class ShopArticleEndpoints(Resource):
    """

    """

    def __init__(self):
        """

        """
        self.shopArticle = ShopArticle()

    def get(self):
        """

        """
        data = request.get_json()
        if data:
            response = jsonify(self.shopArticle.select(data['filter']))
        else:
            response = jsonify(self.shopArticle.select())
        return response

    def post(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.shopArticle.insert(data['body']))
        return response

    def put(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.shopArticle.update(
            data['filter'], data['body']))
        return response

    def delete(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.shopArticle.delete(data['filter']))
        return response
