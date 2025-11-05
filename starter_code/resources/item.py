import collections

# Fix for older Flask/reqparse compatibility
if not hasattr(collections, "Mapping"):
    import collections.abc
    collections.Mapping = collections.abc.Mapping

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from starter_code.models.item import ItemModel


class Item(Resource):
    # renamed to `_parser` so Flask-RESTful won't auto-bind it to all methods
    _parser = reqparse.RequestParser()
    _parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )
    _parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        print("GET endpoint reached for:", name)  # debug confirmation
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"An item with name '{name}' already exists."}, 400

        data = Item._parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except Exception as e:
            print("Error inserting item:", e)
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}

    def put(self, name):
        data = Item._parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": [x.json() for x in ItemModel.query.all()]}
