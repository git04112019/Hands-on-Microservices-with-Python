from flask import Flask

from flask_bootstrap import Bootstrap
from frontend import frontend_blueprint
from user_api import user_api_blueprint
from product_api import product_api_blueprint
from order_api import order_api_blueprint
import models

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@db/order_sys',
))

models.init_app(app)
models.create_tables(app)

app.register_blueprint(frontend_blueprint)
app.register_blueprint(user_api_blueprint)
app.register_blueprint(product_api_blueprint)
app.register_blueprint(order_api_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
