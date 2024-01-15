# from sqlalchemy import Column, Integer, String

# class Category(db.Model):
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)

from dataclasses import dataclass
from extensions import db

@dataclass
class UserInfo(db.Model):
    id : int
    username : str
    password : int
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))