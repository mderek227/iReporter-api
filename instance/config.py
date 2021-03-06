class BaseConfig:
    """Default configuration. Details from this configuration
    class are shared across all environments  """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'qwertyuiopasdfghjklsdfghjklzxcvbnmdfgh'


class DevelopmentConfig(BaseConfig):
    """Development configuration. Loads development configuration data
    when the app is in the development environment"""
    DEBUG = True
    TESTING = False
    ENV = "Development"


class TestingConfig(BaseConfig):
    """Testing configuration. Loads Test configuration data
    when the app is in the Test environment"""
    DEBUG = True
    TESTING = True
    ENV = "Testing"


class ProductionConfig(BaseConfig):
    """Production configuration. Loads Production configuration data
    when the app is in the Production environment"""
    DEBUG = False
    TESTING = False
    ENV = "Production"


app_config = {
            "Development": DevelopmentConfig,
            "Testing": TestingConfig,
            "Production": ProductionConfig
            }
