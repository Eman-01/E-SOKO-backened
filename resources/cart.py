from flask_restful import Resource, reqparse
from models import db, Cart

class CartResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True,
                        help="item name is required")
    
    parser.add_argument('price', type=int, required=True, help="Price is required")
    
    parser.add_argument('image', required=True,
                        help="Image is required")
    
    def get(self, id=None):
        if id == None:
            cart = Cart.query.all()

            
            price = ''


            for cart in cart:
                price.append(cart.to_dict())

            return price
        else:
            cart = Cart.query.filter_by(id=id).first()

            if cart == None:
                return {"message": "Product not added"}, 404

            return cart.to_dict()

    def post(self):
        data = CartResource.parser.parse_args()


        product = Cart(**data)

        db.session.add(product)

        db.session.commit()

        return {"message": "Product added successfully"}


    def delete(self, id):
        cart = Cart.query.filter_by(id=id).first()

        if cart == None:
            return {"message": "Product not added", "status": "fail"}, 404

        db.session.delete(cart)

        db.session.commit()

        return cart
