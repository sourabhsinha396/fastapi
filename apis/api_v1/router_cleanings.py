from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.cleanings import CleaningCreate,CleaningPublic,CleaningInDB,CleaningUpdate
from db.repositories.cleanings import create,get_by_id,list_cleanings,update_clean,delete_

cleaning_router = APIRouter()


@cleaning_router.post("/create/cleanings/",response_model=CleaningPublic)
def create_new_cleaning(new_cleaning: CleaningCreate,db : Session = Depends(get_db)):
    created = create(new_cleaning,db)
    return created


@cleaning_router.get("/cleanings/id/",response_model=CleaningInDB)
def get_cleanings_by_id(num: int, db: Session = Depends(get_db)):
    cleaning = get_by_id(num,db)
    return  cleaning


@cleaning_router.get("/all/")
def get_all_cleanings(db: Session = Depends(get_db)):
    cleanings = list_cleanings(db)
    return cleanings


@cleaning_router.put("/patch/{id}/")
def update_cleaning(id:int,cleaning: CleaningUpdate,db: Session = Depends(get_db)):
    msg = update_clean(id,cleaning,db)
    print("nota")
    return msg


@cleaning_router.delete("/delete/{id}/")
def delete_cleaning(id:int,db: Session = Depends(get_db)):
    msg = delete_(id,db)
    return msg