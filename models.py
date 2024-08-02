from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import check_password_hash
from flask_bcrypt import check_password_hash


# initialize metadata
metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.TIMESTAMP)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'role': self.role
        }

    orders = db.relationship('Order', back_populates='user')
    products = db.relationship('Product', back_populates='user')

    serialize_rules = ('-products.user', '-orders.user', 'password',)
    serialize_only = ('id', 'name', 'email', 'password', 'address')

    cart_products = association_proxy('cart', 'products', creator=lambda product: CartProduct(product=product))

    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)

class Product(db.Model, SerializerMixin):
    __tablename__= 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='products')
    cart = db.relationship('Cart', back_populates='products')

    serialize_rules = ('-user.products', 'cart.products',)
    serialize_only = ('id', 'name', 'description', 'price', 'category', 'image')

class Order(db.Model, SerializerMixin):
    __tablename__= 'orders'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    user = db.relationship('User', back_populates='orders')
    #  orderitems = db.relationship('OrderItem', back_populates='order')

    serialize_rules = ('-user.orders',)
    serialize_only = ('id', 'amount', 'status')

    order_products = association_proxy('products', 'product', creator=lambda product: OrderProduct(product=product))


# class OrderItem(db.Model, SerializerMixin):
#     __tablename__= "orderitems"
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer, nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

#     order = db.relationship('Order', backref='oderitems')

#     serialize_rules = ('-order.orderitems',)

class Cart(db.Model, SerializerMixin):
    __tablename__= 'carts'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

    products = db.relationship('Product', back_populates='cart')

    serialize_rules = ('-products.cart',)
