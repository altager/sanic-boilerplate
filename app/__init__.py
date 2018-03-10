from sanic import Sanic
from sanic_jinja2 import SanicJinja2


jinja = SanicJinja2()


def create_app(config):
    app = Sanic(__name__)
    app.config.from_object(config)
    app.static(config.STATIC_URL, config.STATIC_PATH)

    jinja.init_app(app, pkg_name=__name__)

    register_blueprints(app)

    @app.route('/')
    @jinja.template('index.html')
    async def index(request):
        return

    return app


def register_blueprints(app):
    # Import bp-s from app modules
    from app.sample_module import sample_module

    # Register bp-s
    app.blueprint(sample_module)
