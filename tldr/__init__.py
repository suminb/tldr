import os

from flask import Flask

__version__ = '0.1.1'
__author__ = 'Sumin Byeon'
__email__ = 'suminb@gmail.com'


def create_app(name=__name__, config={}, static_folder='static',
               template_folder='templates'):

    app = Flask(name, static_folder=static_folder,
                template_folder=template_folder)
    app.secret_key = os.environ.get('SECRET', 'secret')
    app.config['DEBUG'] = bool(os.environ.get('DEBUG', False))
    app.config.update(config)

    from tldr.apiv1 import apiv1_module
    app.register_blueprint(apiv1_module, url_prefix='/api/v1/')

    @app.route('/')
    def index():
        return ''

    return app
