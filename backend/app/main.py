from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud, auth
from .database import SessionLocal, engine

# Création des tables à partir des modèles
models.Base.metadata.create_all(bind=engine)

# Initialisation de l'app FastAPI
app = FastAPI()

# Ajout du middleware CORS pour autoriser les requêtes du frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ⚠️ ou ["*"] pour tout autoriser
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dépendance pour obtenir une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========== ROUTES WASTE SPOT ==========
@app.post("/waste-spots/", response_model=schemas.WasteSpot)
def create_waste_spot(spot: schemas.WasteSpotCreate, db: Session = Depends(get_db)):
    return crud.create_waste_spot(db=db, spot=spot)

@app.get("/waste-spots/", response_model=list[schemas.WasteSpot])
def read_waste_spots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_waste_spots(db, skip=skip, limit=limit)

@app.put("/waste-spots/{spot_id}", response_model=schemas.WasteSpot)
def update_spot(spot_id: int, spot: schemas.WasteSpotCreate, db: Session = Depends(get_db)):
    db_spot = crud.update_waste_spot(db, spot_id, spot)
    if not db_spot:
        raise HTTPException(status_code=404, detail="WasteSpot not found")
    return db_spot

@app.delete("/waste-spots/{spot_id}")
def delete_spot(spot_id: int, db: Session = Depends(get_db)):
    db_spot = crud.delete_waste_spot(db, spot_id)
    if not db_spot:
        raise HTTPException(status_code=404, detail="WasteSpot not found")
    return {"message": "Deleted successfully"}

# ========== AUTHENTIFICATION ==========
@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# 🔒 Si besoin tu peux activer les routes externes comme ceci :
# from app.routers import waste_spot
# app.include_router(waste_spot.router)
