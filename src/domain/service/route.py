from typing import List

from fastapi import APIRouter, Depends

from domain.service.schema import Service

router = APIRouter(prefix="/service", tags=["Service"])


@router.get(
    "/all",
    summary="get orders",
    response_model=List[Service],
)
async def get_all():
    return []


@router.put(
    "/sync",
    summary="sync service",
    response_model=List[Service],
)
async def sync():
    return []
