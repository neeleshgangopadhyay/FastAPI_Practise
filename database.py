from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db" ### our database will be inside this directory when we will be running the applivation Okay

### create a database engine for our application and the engine is something we can use in the project shere then.


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread': False})

### create a session locals here
### also making sure that the control fully remains to us here then.
SessionLocal = sessionmaker(autocommit =  False, autoflush =  False, bind = engine)


Base =  declarative_base() ### with thsi we can control our database Okay.

