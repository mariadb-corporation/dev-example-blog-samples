from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mariadb+mariadbconnector://root:password@127.0.0.1:3306/test_2022")
Session = sessionmaker(bind=engine)

Base = declarative_base()
