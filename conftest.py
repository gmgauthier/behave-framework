import configparser
import pytest


config = configparser.ConfigParser()


@pytest.fixture(scope="session", autouse=True)
def headless():
    return _str_to_bool(_read_config_section("fixtures.ini", "dev")["headless"])


def _read_config_section(source, section):
    config.read(source)
    return config[section]


def _str_to_bool(s):
    return s.lower() in ['true', '1', 'yes']
