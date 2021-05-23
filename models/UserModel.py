from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Crear Sesion para conexion a DB
engine = create_engine("mysql+pymysql://root:@localhost/DB_Name")
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()
# Modelo usuario
class c_users(Base):
    __tablename__ = "c_user"
    id = Column(Integer, primary_key=True)
    user = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"id={self.id}, user:{self.user}"
