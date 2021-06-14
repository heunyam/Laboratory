from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mysqlclient는 mysql+mysqldb
DB_URL = 'mysql+mysqldb://root:heunyam@localhost:3306/sqlalchemy-test?charset=utf8mb4'

db_engine = create_engine(DB_URL,  encoding="utf-8",
                          pool_size=20, pool_recycle=3600,
                          max_overflow=20, pool_pre_ping=True)

Session = scoped_session(sessionmaker(bind=db_engine, autocommit=False, autoflush=False))
Base = declarative_base()
session = Session()
