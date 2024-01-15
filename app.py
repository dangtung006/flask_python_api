from flask import Flask

from api.views import blueprint
from extensions import db

app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)
app.config.from_object("config")

db.init_app(app)
app.app_context().push()

#SqlAlchemy Database Configuration With Mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/flask_api?charset=utf8mb4'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000, debug=True)
    app.run(
        host=app.config.get("FLASK_HOST"), 
        port=app.config.get("FLASK_PORT"), 
        debug=app.config.get("FLASK_DEBUG"), 
    )



