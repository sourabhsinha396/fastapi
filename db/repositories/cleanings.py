from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from db.models.cleanings import Cleanings


def create(data: Cleanings,db: Session):
    new_cleaning = Cleanings(name = data.name, description = data.description, cleaning_type = data.cleaning_type.value,price = data.price)
    db.add(new_cleaning)
    db.commit()
    db.refresh(new_cleaning)
    return new_cleaning


def get_by_id(num: int,db: Session):
    cleaning = db.query(Cleanings).filter(Cleanings.id == num).first()
    if not cleaning:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="not found")
    return cleaning


def list_cleanings(db: Session):
    try:
        cleanings = db.query(Cleanings).all()
    except Exception as e:
        print(e)
    return cleanings


def update_clean(id: int, cleaning: Cleanings,db:Session):
    print("updating")
    old_cleaning = db.query(Cleanings).filter(Cleanings.id == id)
    if not cleaning:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog with this id does not exist {id}")
    print("old is",old_cleaning)
    old_cleaning.update(cleaning)
    db.commit()    
    print("yo ho")
    return {"msg":"Successfully updated,enjoy!"}


def delete_(id:int,db:Session):
    cleanings = db.query(Cleanings).filter(Cleanings.id == id)

    if not cleanings.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cleaning with id {id} not found")

    cleanings.delete(synchronize_session=False)
    db.commit()
    return {"msg":"Done deletion"}

#except Exception as e: