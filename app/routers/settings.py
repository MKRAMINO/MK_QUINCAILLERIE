from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict
from .. import crud, dependencies
from ..database import get_db

router = APIRouter(dependencies=[Depends(dependencies.require_admin_role)])

@router.get("/settings/", response_model=Dict[str, str])
def get_all_settings(db: Session = Depends(get_db)):
    return crud.get_settings(db)

@router.post("/settings/", response_model=Dict[str, str])
def update_all_settings(settings_data: Dict[str, str], db: Session = Depends(get_db)):
    return crud.update_settings(db, settings_data)
