from sqlalchemy import Column, Integer, String, ForeignKey, Computed, Double, DateTime
from database import Base


class File(Base):
    __tablename__ = 'file'
    __table_args__ = {'extend_existing': True}
    # Todo: расписать модель