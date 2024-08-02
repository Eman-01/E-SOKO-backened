from flask_restful import Resource, reqparse
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User

class SignupResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Name is required')
    parser.add_argument('email', required=True, help='Email address is required')
    parser.add_argument('password', required=True, help='Password is required')
    parser.add_argument('address', required=True, help='Address is required')
    
    def post(self):
        data = self.parser.parse_args()
        data['password'] = generate_password_hash(data['password'])
        data['role'] = 'member'
        
        email = User.query.filter_by(email=data['email']).first()
        if email:
            return {"message": "Email address already taken", "status": "fail"}, 422
        
        user = User(**data)
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully", "status": "success", "user": user.to_dict()}

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help="Email address is required")
    parser.add_argument('password', required=True, help="Password is required")
    
    def post(self):
        data = self.parser.parse_args()
        user = User.query.filter_by(email=data['email']).first()

        if user:
            is_password_match = user.check_password(data['password'])
            if is_password_match:
                user_dict = user.to_dict()
                additional_claims = {"role": user_dict['role']}
                access_token = create_access_token(identity=user_dict['id'], additional_claims=additional_claims)
                
                db.session.add(user)
                db.session.commit()

                return {"message": "Login successful", "status": "success", "user": user_dict, "access_token": access_token}
            else:
                return {"message": "Invalid email/password", "status": "fail"}, 403
        else:
            return {"message": "Invalid email/password", "status": "fail"}, 403

    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if user:
            return {"message": "User profile fetched successfully", "status": "success", "user": user.to_dict()}
        else:
            return {"message": "User not found", "status": "fail"}, 404
