from flask import request, jsonify
from flask_restful import Resource, abort

from user import users
from model import UserInfo
from extensions import db
from sqlalchemy import select
from sqlalchemy.orm import Session


class Users(Resource):

    def get(self):
        # userss = UserInfo.query.all()
        # return { "data" : userss}
        # return jsonify(data=userss)
    
        try:
            userss = UserInfo.query.all()
            return jsonify(data=userss)
        except Exception as Err:
            message = [str(x) for x in Err.args]
            # print("ERRR : ", Err.NameError)
            return jsonify(Err={"msg" : message })
        # res = []
        # for user in userss:
        #     data = user.serialize()
        #     res.append(data)
        #     print("user : " , data)
    
    def post(self):
        data = request.json
        print(data)
        # last_user_id = users[-1].get("id")

        # new_user = {"id": last_user_id + 1, **data}
        # users.append(new_user)

        # return {"msg": "User created", "user": new_user}

        user = UserInfo(
            username=data.get("username"),
            password=data.get("password")
        )

        db.session.add(user)
        db.session.commit()

        return jsonify(msg="User created", user=user)


class UserResource(Resource):
    def get(self, user_id):
        # user = next(filter(lambda u : u.get("id") == user_id, users), None)

        # if user is None:
        #     abort(404)
        # return { "user" : user}
        try :
            # user = UserInfo.query.get_or_404(user_id)
            user = UserInfo.query.get(user_id)
            # user = UserInfo.query.filter_by(username=="333")
            if user == None:
                raise TypeError("bad request")
            return jsonify(user=user)
        except Exception as Err:
            message = [str(x) for x in Err.args]
            # print("ERRR : ", Err.NameError)
            return jsonify(Err={"msg" : message })
    
    def put(self, user_id):
        # data = request.json
        # user = None

        # for i, u in enumerate(users):
        #     if u.get("id") == user_id:
        #         users[i] = {**u, **data}
        #         user = users[i]

        # if user  == None:
        #     abort(404)
        # return {"msg": "User updated", "user": user}

        data = request.json

        user = UserInfo.query.get_or_404(user_id)
        user.username = data.get("username")
        user.password = data.get("password")
        db.session.commit()

        return jsonify(msg="User updated", user=user)

    def delete(self, user_id):
        # user = None

        # for i, u in enumerate(users):
        #     if u.get("id") == user_id:
        #         user = u
        #         users.pop(i)

        # if user is None:
        #     abort(404)

        # return {"msg": "User deleted"}
        user = UserInfo.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return jsonify(msg="User deleted")