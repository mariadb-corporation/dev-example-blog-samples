from datetime import date

from base import Session, engine, Base
from MetaData import FileData
from MetaData import ExifData

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

session.commit()
session.close()
