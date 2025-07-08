import pytest


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass
    # def setup_method(self,method):
    #     logger = generate_logger(self.__class__.__name__)
    #     return logger
