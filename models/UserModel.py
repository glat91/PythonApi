from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/facturacion")
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()

class cat_users_new(Base):
    __tablename__ = "cat_users_new"
    id = Column(Integer, primary_key=True)
    user = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"id={self.id}, user:{self.user}"