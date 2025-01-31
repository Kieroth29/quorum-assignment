from typing import List

from fastapi import APIRouter

from schemas.bill import Bill
from schemas.legislator import Legislator
from services.bill import BillService
from services.legislator import LegislatorService


router = APIRouter(prefix='/legislation')

bill_service = BillService()
legislator_service = LegislatorService()


@router.get('/legislators')
async def list_legislators() -> List[Legislator]:
    return legislator_service.list_legislators()


@router.get('/bills')
async def list_bills() -> List[Bill]:
    return bill_service.list_bills()
