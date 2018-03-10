"""

Predefined configurations

"""


class BaseConfig:
    HOST = '0.0.0.0'
    PORT = '8000'
    STATIC_URL = '/static'
    STATIC_PATH = './static'


class Debug(BaseConfig):
    DEBUG = True


class Prod(BaseConfig):
    DEBUG = False


config = {
    'debug': Debug,
    'prod': Prod
}