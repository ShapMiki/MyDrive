from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Computed, Double, DateTime
from sqlalchemy.orm import relationship
from database import Base

from data.local_data_manager import server_config
from association.tables import (
    favorite_files_association,
    favorite_directions_association,
    direction_coloborators_association
)

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    surname = Column(String)
    telephone = Column(String)
    email = Column(String)
    password = Column(String, nullable=False)
    root = Column(Boolean, default=False, nullable=False)
    image_src = Column(String, default='default.png', nullable=False)
    description = Column(String, default='', nullable=False)
    space_volume = Column(Double, default=server_config.default_user_space_volume, nullable=False)

    files = relationship("File", back_populates="owner", cascade="all, delete-orphan")
    directions = relationship("Direction", back_populates="owner", cascade="all, delete-orphan")
    
    general_directions = relationship(
        "Direction",
        secondary=direction_coloborators_association,
        back_populates="general_users"
    )
    favorite_directions = relationship(
        "Direction",
        secondary=favorite_directions_association,
        back_populates="favorite_users"
    )
    favorite_files = relationship(
        "File",
        secondary=favorite_files_association,
        back_populates="favorite_users"
    )


