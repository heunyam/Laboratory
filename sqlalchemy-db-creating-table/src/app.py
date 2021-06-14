from src.models import Base, db_engine, session
from src.models.user import UserModel


if __name__ == '__main__':
    Base.metadata.drop_all(bind=db_engine)

