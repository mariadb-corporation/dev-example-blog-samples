from datetime import date

from base import Session, engine, Base
from dbschema import Asset
from dbschema import Model
from dbschema import AssetTyp
from dbschema import Computer

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Asset Typen erstellen
asset_typ1 = AssetTyp(name='Computer')
asset_typ2 = AssetTyp(name='Laptop')

# Model erstellen
model1 = Model(bezeichnung='TestComputer', typ=asset_typ1)
model2 = Model(bezeichnung='TestLaptop', typ=asset_typ2)

# Asset erstellen
asset1 = Asset(model=model1)

# Computer erstellen
computer1 = Computer(assets=asset1, pcname='TestRechner')

# Asset Typen hinzufügen
session.add(asset_typ1)
session.add(asset_typ2)

session.add(model1)
session.add(model2)

session.add(asset1)

session.add(computer1)

session.commit()
session.close()