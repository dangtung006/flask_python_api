# from sqlalchemy import Column, Integer, String

# class Category(db.Model):
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)

from app import db
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
 
 
    def __init__(self, username, password):
        self.username = username
        self.password = password