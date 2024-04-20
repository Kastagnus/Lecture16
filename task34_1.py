from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

database = "mysql+pymysql://root:Navigacia1@127.0.0.1:3306/it_step34"
engine = create_engine(database, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), primary_key=True)
    profile = relationship('Profile', back_populates='user', uselist=False)

class Profile(Base):
    __tablename__ = 'profile_name'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bio = Column(String(100))
    profile_picture = Column(String(200))
    user_name = Column(String(150), ForeignKey('user.user_name'), unique=True)
    user = relationship('User', back_populates='profile')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
