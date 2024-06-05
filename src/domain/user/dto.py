from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class BaseUser(BaseModel):
    name: str
    email: EmailStr


class User(BaseUser):
    id: int = Field(
        default=None,
        primary_key=True
    )
    password: str
    is_active: bool = True
    created_at: datetime = Field(
        default_factory=datetime.now
    )
    updated_at: datetime = Field(
        default_factory=datetime.now
    )
    deleted_at: datetime | None = None

    class Config:
        from_attributes = True


class CreateUser(BaseUser):
    password: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str

    def is_passwords_match(self):
        return self.new_password == self.confirm_password
