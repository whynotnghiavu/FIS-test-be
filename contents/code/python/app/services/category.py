from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import category as _schemas_category


from ..models.category import Category as _models_category


def create(category: _schemas_category.CategoryCreate, db: Session):
    db_category = db.query(_models_category).filter(_models_category.name == category.name).first()
    if db_category:
        raise HTTPException(status_code=400, detail=f"Category with name '{category.name}' already exists.")

    new_category = _models_category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(_models_category).offset(skip).limit(limit).all()


def get_by_id(category_id: int, db: Session):
    return db.query(_models_category).filter(_models_category.id == category_id).first()


def update(category_id: int, category: _schemas_category.CategoryUpdate, db: Session):
    db_category = db.query(_models_category).filter(_models_category.id == category_id).first()
    if db_category is None:
        return None

    if category.name:
        existing_category = db.query(_models_category).filter(
            _models_category.name == category.name,
            _models_category.id != category_id
        ).first()

        if existing_category:
            raise HTTPException(status_code=400, detail=f"Category with name '{category.name}' already exists.")

    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def remove(category_id: int, db: Session):
    db_category = db.query(_models_category).filter(_models_category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return
    raise HTTPException(status_code=404, detail="Category not found")
