from fastapi import APIRouter
from backend.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
async def dashboard_stats():

    return DashboardService.get_stats()