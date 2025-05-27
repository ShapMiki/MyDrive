from sqlalchemy import Column, Integer, String, ForeignKey, Computed, Double, DateTime
from database import Base


class Direction(Base):
    __tablename__ = 'direction'
    __table_args__ = {'extend_existing': True}
    #Todo: расписать модель