import os
import sys

from app import create_app
from config import config


if __name__ == '__main__':
    conf_env = os.getenv("APP_CONFIG")
    app_config = config[conf_env] if conf_env else config[sys.argv[1]]
    create_app(config=app_config).run(host=app_config.HOST, port=app_config.PORT, debug=app_config.DEBUG)
