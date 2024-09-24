from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..schemas import user as _schemas_user


from .. import models


from . import auth
from . import manager_password


def create_superuser(user: _schemas_user.UserRegister, db: Session):
    count_user = db.query(models.User).count()

    if count_user == 0:
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail=f"Email '{user.email}' already exists.")

        user.password = manager_password.hash_password(user.password)
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)





def login(user: _schemas_user.UserLogin, db: Session):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Incorrect login information")

    if not manager_password.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail=f"Incorrect login information")

    return auth.generate_token(db_user)



# def register(user: _schemas_user.UserRegister, db: Session):
#     db_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail=f"Email '{user.email}' already exists.")

#     user.password = manager_password.hash_password(user.password)
#     new_user = models.User(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return auth.generate_token(new_user)

