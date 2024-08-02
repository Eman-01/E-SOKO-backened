from flask_restful import Resource, reqparse
from models import db, Product


class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True,
                        help="Product name is required")
    parser.add_argument('description', required=True,
                        help="Description is required")
    parser.add_argument('price', type=int, required=True, help="Price is required")
    parser.add_argument('category', required=True,
                        help="Category is required")
    parser.add_argument('image', required=True,
                        help="Image is required")
 
    

    
    def get(self, id=None):
        if id == None:
            products = Product.query.all()
            price = []

            for product in products:
                price.append(product.to_dict())

            return price
        else:
            product = Product.query.filter_by(id=id).first()

            if product == None:
                return {"message": "Product not found"}, 404

            return product.to_dict()

    def post(self):
        data = ProductResource.parser.parse_args()


        product = Product(**data)

        db.session.add(product)

        db.session.commit()

        return {"message": "Product posted successfully"}


    def delete(self, id):
        product = Product.query.filter_by(id=id).first()

        if product == None:
            return {"message": "Product not found", "status": "fail"}, 404

        db.session.delete(product)

        db.session.commit()

        return product