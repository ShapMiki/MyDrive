from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import Optional
from fastapi import UploadFile, Form


class SUserRegistrate(BaseModel):
    name: str = Field(..., min_length=2, max_length=30)
    surname: Optional[str] = Field(None, min_length=1, max_length=30)
    telephone: Optional[str] = Field(None, min_length=9, max_length=13)
    email: Optional[EmailStr] = Field(None, min_length=1, max_length=50)
    password: str = Field(..., min_length=8, max_length=50)


class SUserLogin(BaseModel):
    namespace: str
    password: str
