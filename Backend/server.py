from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

#Connecting with the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/flask_authenticcate_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Handling cross-origin requests
CORS(app)


#User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        data = parser.parse_args()

        name = data['name']
        email = data['email']
        password = data['password']

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        data = parser.parse_args()

        email = data['email']
        password = data['password']

        # Check if the user exists in the database
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            # User authentication successful
            return {'message': 'Login successful'}, 200
        else:
            # User authentication failed
            return {'message': 'Invalid email or password'}, 401
        
api.add_resource(Register, '/register')
api.add_resource(Login,'/login')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)