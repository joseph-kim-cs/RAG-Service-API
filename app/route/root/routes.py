from fastapi import APIRouter, requests as request
from fastapi.responses import HTMLResponse

root_api_route = APIRouter()

@root_api_route.get("/", response_class=HTMLResponse)
def root_api():
    return "<h2>Welcome to the RAG Accelerator API!</h2>"
    