from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas, dependencies
from ..database import get_db

router = APIRouter()

@router.post("/orders/", response_model=schemas.PurchaseOrder, dependencies=[Depends(dependencies.require_admin_role)])
def create_purchase_order(order: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    return crud.create_purchase_order(db=db, order=order)

@router.get("/orders/", response_model=List[schemas.PurchaseOrder], dependencies=[Depends(dependencies.require_admin_role)])
def read_purchase_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_purchase_orders(db, skip=skip, limit=limit)

@router.post("/orders/{order_id}/receive", response_model=schemas.PurchaseOrder, dependencies=[Depends(dependencies.require_admin_role)])
def receive_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.receive_purchase_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found or already received")
    return db_order
