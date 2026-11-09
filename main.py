from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
PAGES_DIR = BASE_DIR / "pages"

PROJECT_PAGES = {
    "interviewai": "interviewai.html",
    "justmobile": "justmobile.html",
    "taskflow-api": "taskflow-api.html",
    "faceattend": "faceattend.html",
}

app = FastAPI(title="Mahammad Thameez — Portfolio")
app.mount("/assets", StaticFiles(directory=BASE_DIR / "assets"), name="assets")


@app.get("/", include_in_schema=False)
def read_root() -> FileResponse:
    return FileResponse(BASE_DIR / "index.html")


@app.get("/about", include_in_schema=False)
def read_about() -> FileResponse:
    return FileResponse(PAGES_DIR / "about.html")


@app.get("/projects/{slug}", include_in_schema=False)
def read_project(slug: str) -> FileResponse:
    page = PROJECT_PAGES.get(slug)
    if page is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return FileResponse(PAGES_DIR / "projects" / page)


@app.get("/resume", include_in_schema=False)
def download_resume() -> FileResponse:
    return FileResponse(
        BASE_DIR / "resume.pdf",
        media_type="application/pdf",
        filename="Mahammad-Thameez-Resume.pdf",
    )
