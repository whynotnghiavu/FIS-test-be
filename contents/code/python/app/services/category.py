from fastapi import HTTPException,status
from sqlalchemy.orm import Session


from ..schemas import category as _schemas_category

from .. import models


def create(category: _schemas_category.CategoryCreate, db: Session):
    db_category = db.query(models.Category).filter(models.Category.name == category.name).first()
    if db_category:
        raise HTTPException(status_code=400, detail=f"Category with name '{category.name}' already exists.")

    new_category = models.Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_by_id(category_id: int, db: Session):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def update(category_id: int, category: _schemas_category.CategoryUpdate, db: Session):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    if category.name:
        existing_category = db.query(models.Category).filter(
            models.Category.name == category.name,
            models.Category.id != category_id
        ).first()

        if existing_category:
            raise HTTPException(status_code=400, detail=f"Category with name '{category.name}' already exists.")

    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def remove(category_id: int, db: Session):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    db.delete(db_category)
    db.commit()
    return
