import tomllib


def get_settings() -> dict:
    with open('settings.toml', 'rb') as settings_file:
        config = tomllib.load(settings_file)['settings']
    return config
