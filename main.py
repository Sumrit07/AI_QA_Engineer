from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config.settings import settings
from backend.config.logger import app_logger

from backend.database.database import engine
from backend.database.base import Base

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from fastapi import Depends
from backend.dependencies.auth import get_current_user

# Import Models (IMPORTANT)
from backend.models.project import Project
from backend.models.report import Report

# Import Routers
from backend.api.project_routes import router as project_router
from backend.api.upload_routes import router as upload_router
from backend.api.bugfix import router as bugfix_router
from backend.api.ai_routes import router as ai_router
from backend.api.project_analysis_routes import router as project_analysis_router
from backend.api.report_routes import router as report_router
from backend.api.dashboard_routes import router as dashboard_router
from backend.api.auth import router as auth_router


from fastapi.staticfiles import StaticFiles




app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI QA Platform"
)


app.mount("/static", StaticFiles(directory="frontend"), name="static")


app.mount(
    "/fixed_projects",
    StaticFiles(directory="fixed_projects"),
    name="fixed_projects"
)


@app.get("/")
async def home():
    return FileResponse("frontend/login.html")
    
@app.get("/login")
async def login_page():
    return FileResponse("frontend/login.html")


@app.get("/dashboard")
async def dashboard():
    return FileResponse("frontend/dashboard.html")

app.mount(
    "/report_files",
    StaticFiles(directory="reports"),
    name="report_files"
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(project_router)
app.include_router(upload_router)
app.include_router(bugfix_router)
app.include_router(ai_router)
app.include_router(project_analysis_router)
app.include_router(report_router)
app.include_router(dashboard_router)
app.include_router(auth_router)




# -----------------------------
# Startup
# -----------------------------
@app.on_event("startup")
async def startup():

    app_logger.info("Application Started")

    # Create Database Tables
    Base.metadata.create_all(bind=engine)

    app_logger.info("Database Connected Successfully")
    app_logger.info("AI QA Engineer Started")
