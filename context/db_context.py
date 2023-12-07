from sqlmodel import Field, Session, SQLModel, create_engine, select

class DBContext(object):
    _instance = None

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

    SQLModel.metadata.create_all(engine)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
