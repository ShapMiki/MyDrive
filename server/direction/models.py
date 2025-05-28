from sqlalchemy import Column, Integer, String, ForeignKey, Computed, Double, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base

from data.local_data_manager import server_config
from utils.key_generators import generate_link_key
from association.tables import (
    favorite_directions_association,
    direction_coloborators_association
)


class Direction(Base):
    __tablename__ = 'direction'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship("User", back_populates="directions")
    srс = Column(String, nullable=False)

    color = Column(String, default="black", nullable=False)
    coloborators = relationship(
        "User",
        secondary=direction_coloborators_association,
        back_populates="collaborated_directions"
    )

    create_root = Column(Boolean, default=False, nullable=False)
    delete_root = Column(Boolean, default=False, nullable=False)
    edit_root = Column(Boolean, default=False, nullable=False)
    donwload_root = Column(Boolean, default=False, nullable=False)

    is_general = Column(Boolean, default=False, nullable=False)
    is_open_source = Column(Boolean, default=False, nullable=False)

    coloborators_space_volume = Column(Double, default=server_config.default_coloborators_space_volume, nullable=False)

    direction_continue = Column(Integer, ForeignKey('direction.id'))
    link_key = Column(String, default=generate_link_key, nullable=False)

    parent_id = Column(Integer, ForeignKey('direction.id'))
    parent = relationship(
        "Direction",
        remote_side=[id],
        back_populates="children",
        foreign_keys=[parent_id]
    )

    children = relationship(
        "Direction",
        back_populates="parent",
        foreign_keys=[parent_id]
    )

    favorite_users = relationship(
        "User",
        secondary=favorite_directions_association,
        back_populates="favorite_directions"
    )

