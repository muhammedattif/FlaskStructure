import os

class Config(object):
    """
    Global Configurations

    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(16)
    SESSION_COOKIE_SECURE = True
    SERVER_NAME = '10.0.0.5:5000'
    TRAP_HTTP_EXCEPTIONS = True


class production(Config):
    """
    Configurations for Production Environment
    """
    ENV = 'production'


class development(Config):
    """
    Configurations for Development Environment
    """

    DEBUG = True
    ENV = 'development'



class testing(Config):
    """
    Configurations for Testing Environment
    """
    TESTING = True
    ENV = 'testing'
    SESSION_COOKIE_SECURE = True
