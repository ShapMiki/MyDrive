from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base

favorite_files_association = Table(
    'favorite_files_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('file_id', Integer, ForeignKey('file.id'), primary_key=True)
)

favorite_directions_association = Table(
    'favorite_directions_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('direction_id', Integer, ForeignKey('direction.id'), primary_key=True)
)

direction_coloborators_association = Table(
    'direction_coloborators_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('direction_id', Integer, ForeignKey('direction.id'), primary_key=True)
) 