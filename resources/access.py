from flask import request
from flask_restful import reqparse, fields, Resource
from models.UserModel import cat_users_new, session

user_args = reqparse.RequestParser()
user_args.add_argument("user", type=str, help="Need user", required=True)
user_args.add_argument("password", type=str, help="Need pass", required=True)

class Access(Resource):
    def post(self):
        args = user_args.parse_args()
        result = session.query(cat_users_new).filter(cat_users_new.user == args['user']).first()
        print(result)

        if result == None:
            return {"message": "User or Password are incorrect"}, 203
        print( {"token":result})
        return {"token":str(result)}, 200

    def put(self):
        r = request.form
        new_user = cat_users_new(user=r["user"], password=r["password"])
        # update
        session.add(cat_users_new)
        session.commit()
        return r
