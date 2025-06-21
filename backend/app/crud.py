from sqlalchemy.orm import Session
from . import models, schemas
from .models import User
from passlib.context import CryptContext

def get_waste_spots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WasteSpot).offset(skip).limit(limit).all()

def get_waste_spot(db: Session, spot_id: int):
    return db.query(models.WasteSpot).filter(models.WasteSpot.id == spot_id).first()

def create_waste_spot(db: Session, spot: schemas.WasteSpotCreate):
    db_spot = models.WasteSpot(**spot.dict())
    db.add(db_spot)
    db.commit()
    db.refresh(db_spot)
    return db_spot

def update_waste_spot(db: Session, spot_id: int, spot: schemas.WasteSpotCreate):
    db_spot = get_waste_spot(db, spot_id)
    if db_spot:
        db_spot.location = spot.location
        db_spot.photo_url = spot.photo_url
        db_spot.status = spot.status
        db.commit()
        db.refresh(db_spot)
    return db_spot

def delete_waste_spot(db: Session, spot_id: int):
    db_spot = get_waste_spot(db, spot_id)
    if db_spot:
        db.delete(db_spot)
        db.commit()
    return db_spot

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user):
    hashed_pw = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user