from sqlalchemy import Column, Integer, String, ForeignKey, Computed, Double, DateTime
from database import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    # Todo: расписать модель