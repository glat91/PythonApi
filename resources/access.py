lfrom flask import request
from flask_restful import reqparse, fields, Resource
from models.UserModel import c_users, session

user_args = reqparse.RequestParser()
user_args.add_argument("user", type=str, help="Need user", required=True)
user_args.add_argument("password", type=str, help="Need pass", required=True)

class Access(Resource):
    def post(self):
        args = user_args.parse_args()
        # Query
        result = session.query(c_users).filter(c_users.user == args['user']).first()
        if result == None:
            return {"message": "User or Password are incorrect"}, 203
        return {"result":str(result)}, 200

    def put(self):
        r = request.form
        new_user = c_users(user=r["user"], password=r["password"])
        # update
        session.add(c_users)
        session.commit()
        return r
