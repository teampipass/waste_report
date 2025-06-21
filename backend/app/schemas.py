from pydantic import BaseModel, EmailStr
##from pydantic_settings import SettingsConfigDict

class WasteSpotBase(BaseModel):
    location: str
    photo_url: str
    status: str = "nouveau"

class WasteSpotCreate(WasteSpotBase):
    pass

class WasteSpot(WasteSpotBase):
    id: int
    user_id: int
class Config:
    from_attributes = True
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    ##model_config = SettingsConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
