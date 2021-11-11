import configparser


def get_config() -> configparser.SectionProxy:
    config: ConfigParser = configparser.ConfigParser()
    config.read('config/config.ini')

    profile: str = config['PROGRAM']['Profile']

    return config[profile]

