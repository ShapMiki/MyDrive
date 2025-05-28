from sqlalchemy import Column, Integer, String, ForeignKey, Computed, Double, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base

from utils.key_generators import generate_link_key
from association.tables import favorite_files_association



class File(Base):
    __tablename__ = 'file'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    owner = relationship("User", back_populates="files")
    name = Column(String, default="noname", nullable=False)
    type = Column(String, default=".none", nullable=False)
    description = Column(String, default="", nullable=False)
    compressed = Column(Boolean, default=False, nullable=False)
    src = Column(String)
    size = Column(Double, default=0.0, nullable=False)
    share_key = Column(String, default=generate_link_key, nullable=False)

    favorite_users = relationship(
        "User",
        secondary=favorite_files_association,
        back_populates="favorite_files"
    )
    