from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from .. import crud, models, schemas, dependencies
from ..database import get_db

router = APIRouter(dependencies=[Depends(dependencies.require_admin_role)])

@router.get("/dashboard/kpis", response_model=dict)
def get_dashboard_kpis(db: Session = Depends(get_db)):
    return crud.get_dashboard_kpis(db)

@router.get("/dashboard/low-stock", response_model=List[schemas.Product])
def get_low_stock_products(db: Session = Depends(get_db)):
    return crud.get_low_stock_products(db)

@router.get("/dashboard/recent-sales", response_model=List[schemas.Sale])
def get_recent_sales(db: Session = Depends(get_db)):
    return crud.get_sales(db, limit=5)

@router.get("/finances/kpis", response_model=dict)
def get_finance_kpis(db: Session = Depends(get_db)):
    return crud.get_finance_kpis(db)

@router.get("/finances/monthly-chart", response_model=List[float])
def get_monthly_chart_data(year: int = datetime.now().year, db: Session = Depends(get_db)):
    return crud.get_monthly_sales_chart_data(db, year)
