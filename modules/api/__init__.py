"""Module for starting app"""

from flask import Flask


def create_app(test_config=None) -> Flask:
    """
    Creates app

    :param test_config: config for the flask app
    :return: app function
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    from modules.api import routes
    app.register_blueprint(routes.blue_print)

    app.add_url_rule('/', endpoint='index')

    return app
