from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from models import db
from resources.product import ProductResource
from resources.order import OrderResource
from resources.cart import CartResource
from resources.user import SignupResource, LoginResource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)


migrate = Migrate(app, db, render_as_batch=True)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


db.init_app(app)

api.add_resource(ProductResource, '/products', '/products/<int:id>')
api.add_resource(CartResource, '/carts', '/carts/<int:id>')
api.add_resource(OrderResource, '/orders', '/orders/<int:id>')
api.add_resource(SignupResource, '/signup')
api.add_resource(LoginResource, '/login')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
