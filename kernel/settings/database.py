from .base import config


# DB info
DB_CONF: dict = config['database']
DB_NAME: str = DB_CONF['DB_NAME']
DB_USER: str = DB_CONF['DB_USER']
DB_PASSWORD: str = DB_CONF['DB_PASSWORD']
DB_PORT: int = DB_CONF['DB_PORT']
DB_HOST: str =  DB_CONF['DB_HOST']

DB_URL: str = \
f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
