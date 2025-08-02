from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas, dependencies
from ..database import get_db

router = APIRouter()

@router.post("/suppliers/", response_model=schemas.Supplier, dependencies=[Depends(dependencies.require_admin_role)])
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db=db, supplier=supplier)

@router.get("/suppliers/", response_model=List[schemas.Supplier])
def read_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_active_user)):
    suppliers = crud.get_suppliers(db, skip=skip, limit=limit)
    return suppliers

@router.get("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_active_user)):
    db_supplier = crud.get_supplier(db, supplier_id=supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.put("/suppliers/{supplier_id}", response_model=schemas.Supplier, dependencies=[Depends(dependencies.require_admin_role)])
def update_supplier(supplier_id: int, supplier_update: schemas.SupplierUpdate, db: Session = Depends(get_db)):
    db_supplier = crud.update_supplier(db, supplier_id, supplier_update)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.delete("/suppliers/{supplier_id}", response_model=schemas.Supplier, dependencies=[Depends(dependencies.require_admin_role)])
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud.delete_supplier(db, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier
