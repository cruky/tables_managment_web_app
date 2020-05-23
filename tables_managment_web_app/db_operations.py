from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Float, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import NullType
from datetime import datetime

def get_session(echo=False):
    engine = create_engine('sqlite:///assets_database.db', echo=echo)
    DBSession = sessionmaker(bind=engine)
    return DBSession()

Base = declarative_base()


class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True)
    source_id = Column(Text)
    type = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    owner = Column(Text)
    date = Column(Text)

    def __repr__(self):
        return f'type:{self.type} latitude:{self.latitude} longitude:{self.longitude}'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)


def add_asset(session, source_id, type, latitude, longitude, owner):
    '''Add new asset to the database '''

    new_asset = Asset(source_id=source_id, type=type, latitude=latitude, longitude=longitude, owner=owner, date=datetime.now())
    session.add(new_asset)
    session.commit()


def get_count_of_db(session):
    '''Return count from Asset db'''
    return session.query(func.count(Asset.id)).scalar()

def get_all_rows_from_assets(session):
    return session.query(Asset).all()