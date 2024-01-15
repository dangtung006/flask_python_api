from dotenv import load_dotenv
import os
load_dotenv()

FLASK_HOST= os.environ.get("FLASK_HOST")
FLASK_PORT= os.environ.get("FLASK_PORT")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
ENV = os.environ.get("ENV")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS= os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")