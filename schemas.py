from pydantic import BaseModel, EmailStr, Field, constr
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    # Password truncated to 72 characters to satisfy bcrypt limitation
    password: constr(min_length=6, max_length=72)

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True  # Replaces orm_mode in Pydantic v2
    }
