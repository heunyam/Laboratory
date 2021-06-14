from . import Base
from sqlalchemy import Column, String, CHAR


class UserDefaultValue:
    image = 'default.png'
    introduction = ''


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String(45), nullable=False, primary_key=True)
    password = Column(CHAR(94), nullable=False)
    name = Column(String(45), nullable=False)
    img = Column(String(100), nullable=True, server_default=UserDefaultValue.image)

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
