from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from helpers.designs import Singleton
from kernel.settings import DB_URL


class SqlAlchemy(metaclass=Singleton):
    def __init__(self) -> None:
        self.engine = self.create_engine()
        self.session = self.create_session()

    def create_engine(self) -> Engine:
        engine = create_engine(DB_URL)
        return engine

    def create_session(self) -> Session:
        session = Session(self.engine)
        return session
