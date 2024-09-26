import re
from pydantic import BaseModel, field_validator


from ..models import Role


class UserBase(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def email_validator(cls, email):
        if email == "":
            raise ValueError("Email must not be empty")

        email_regex = re.compile(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$')
        if not email_regex.match(email):
            raise ValueError("Invalid email format")

        return email

    @field_validator("password")
    def password_validator(cls, password):
        if len(password) < 8:
            raise ValueError("Password length must be greater than 8 characters")

        password_regex = re.compile(r'^(?!.*[_;*\'"`])(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{8,}$')
        if not password_regex.match(password):
            raise ValueError("Invalid password format")

        return password


class UserRegister(UserBase):
    role: Role


class UserLogin(UserBase):
    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "email": "admin@gmail.com",
    #                 "password": "admin@A8"
    #             }
    #         ]
    #     }
    # }
    pass


class User(UserBase):
    id: int
    role: Role

    class Config:
        # orm_mode = True
        from_attributes = True


class JWTUser(User):
    user_id: int
    role: Role
    jwt_expire: str
    otp_expire: str
