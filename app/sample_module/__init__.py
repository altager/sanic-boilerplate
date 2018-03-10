from sanic import Blueprint

sample_module = Blueprint('sample_module')

from app.sample_module import views