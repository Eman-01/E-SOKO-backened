from flask_restful import Resource, reqparse
from models import db, Order


class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('amount', type=int, required=True, help="Amount is required")
    parser.add_argument('status', required=True,
                        help="Status is required")

    
    def get(self, id=None):
        if id == None:
            orders = Order.query.all()
            amount = []

            for order in orders:
                amount.append(order.to_dict())

            return amount
        else:
            order = Order.query.filter_by(id=id).first()

            if order == None:
                return {"message": "Order not found"}, 404

            return order.to_dict()

    def post(self):
        data = OrderResource.parser.parse_args()


        order = Order(**data)

        db.session.add(order)

        db.session.commit()

        return {"message": "Order created successfully"}


    def delete(self, id):
        order = Order.query.filter_by(id=id).first()

        if order == None:
            return {"message": "Order not found", "status": "fail"}, 404

        db.session.delete(order)

        db.session.commit()

        return order