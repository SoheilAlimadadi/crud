from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from helpers.designs import Singleton
from kernel.settings.database import DB_URL


class SqlAlchemy(metaclass=Singleton):
    """
    A singleton class for creating a SQLAlchemy engine and session.

    This class provides a single instance of a SQLAlchemy engine and session
    that can be used throughout the application. It uses the Singleton pattern
    to ensure that only one instance of the class is created.

    Attributes
    ----------
    engine : Engine
        The SQLAlchemy engine instance.
    session : Session
        The SQLAlchemy session instance.
    base:
        The model declarative base

    Methods
    -------
    create_engine() -> Engine:
        Creates a new SQLAlchemy engine instance.
    create_session() -> Session:
        Creates a new SQLAlchemy session instance.

    Examples
    --------
    >>> db = SqlAlchemy()
    >>> engine = db.engine
    >>> session = db.session
    """

    def __init__(self) -> None:
        """
        Initializes the SqlAlchemy instance.

        Creates a new SQLAlchemy engine and session instance.
        """
        self.engine = self.create_engine()
        self.session = self.create_session()
        self.Base = declarative_base()

    def create_engine(self) -> Engine:
        """
        Creates a new SQLAlchemy engine instance.

        Returns
        -------
        Engine
            A new SQLAlchemy engine instance.
        """
        engine = create_engine(DB_URL)
        return engine

    def create_session(self) -> Session:
        """
        Creates a new SQLAlchemy session instance.

        Returns
        -------
        Session
            A new SQLAlchemy session instance.
        """
        session = Session(self.engine)
        return session
