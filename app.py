# from flask import Flask

# app = Flask(__name__)
# app.register_blueprint(blueprint=blueprint)
# app.config.from_object("config")


from flask import Flask
# from api.views import blueprint
# from extensions import db
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.register_blueprint(blueprint=blueprint)
# app.config.from_object("config")

# app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost/flask_api?charset=utf8mb4"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/flask_api?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



