from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from validators import ScrapeInputValidator
from utils import search_github, search_gitlab, search_indexed_google, search_stack_exchange, search_vimeo


scrape_router = APIRouter(
    prefix="/scrape",
    tags=["Income Tracker Router APIs"]
)


@scrape_router.post("/github", status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    github_links = search_github(data)
    return data

@scrape_router.post("/gitab", status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    github_links = search_gitlab(data)
    return data

@scrape_router.post("/stack-overflow", status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    github_links = search_stack_exchange(data)
    return data

@scrape_router.post("/vimeo", status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    github_links = search_vimeo(data)
    return data

@scrape_router.post("/google-index", status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    github_links = search_indexed_google(data)
    return data