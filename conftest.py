import configparser
import pytest

import fixtures

config = configparser.ConfigParser()


def pytest_addoption(parser):
    """ attaches optional cmd-line args to the pytest machinery """
    parser.addoption('--properties',
                     action='store',
                     default='staging',
                     help='the name of the environment for which you need properties.')
    parser.addoption('--fixture',
                     action='store',
                     default='default',
                     help='the name of the environment for which you need fixture accounts.')


@pytest.fixture(scope="session", autouse=True)
def service_base_url(pytestconfig):
    """
    The url of the live sme-service under test
    """
    env = pytestconfig.getoption("env")
    return _read_config_section(fixtures, env)['target_url']


@pytest.fixture(scope="session", autouse=True)
def fixture_data(pytestconfig):
    """
    The fixture data items for the account under test
    """
    #env = pytestconfig.getoption("env")
    return _read_config_section(fixtures, "env")


def _read_config_section(source, section):
    config.read(source)
    return config[section]


def _read_fixture_file(fixtures):
    fixture_data = config.read(fixtures)
    return fixture_data
