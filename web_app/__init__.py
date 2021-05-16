# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.currency_routes import currency_routes
# deleted book_routes

load_dotenv()

#creating app / setting up blueprint files for specific routes
def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(currency_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)