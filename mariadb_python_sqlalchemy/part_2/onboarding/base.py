from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mariadb+mariadbconnector://app_user:Password123!@127.0.0.1:3306/planning")
Session = sessionmaker(bind=engine)

Base = declarative_base()