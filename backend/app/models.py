from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class WasteSpot(Base):
    __tablename__ = "waste_spots"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String(255))
    photo_url = Column(String(255))
    status = Column(String(50), default="nouveau")
    user_id = Column(Integer, ForeignKey("users.id"))
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
