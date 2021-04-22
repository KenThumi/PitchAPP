class Config:
    '''General configuration parent class'''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    '''
    Test  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}