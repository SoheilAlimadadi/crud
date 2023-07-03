class DataAccessError(Exception):
    """Base exception for data access errors."""
    pass

class RetrievalError(DataAccessError):
    """Exception for errors that occur when retrieving data from the database."""
    pass

class CreationError(DataAccessError):
    """Exception for errors that occur when creating data in the database."""
    pass

class UpdateError(DataAccessError):
    """Exception for errors that occur when updating data in the database."""
    pass

class DeletionError(DataAccessError):
    """Exception for errors that occur when deleting data from the database."""
    pass
