from fastapi import APIRouter, status, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from validators import ScrapeInputValidator
from utils import search_github, search_gitlab, search_indexed_google, search_stack_exchange, search_vimeo
from auth import authenticate



async def convert_data_to_dict(data):
    return {
        "first_name":data.first_name,
        "last_name":data.last_name,
        "email":data.email,
        "phone":data.phone,
        "country":data.country
    }



scrape_router = APIRouter(
    prefix="/scrape",
    tags=["Income Tracker Router APIs"]
)


@scrape_router.post("/github", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    user_data =  await convert_data_to_dict(data)
    github_links = search_github(user_data)
    return github_links

@scrape_router.post("/gitlab", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_gitlab_profiles(data:ScrapeInputValidator):
    user_data =  await convert_data_to_dict(data)
    gitlab_links = search_gitlab(user_data)
    return gitlab_links

@scrape_router.post("/stack-overflow", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_stack_overflow_profiles(data:ScrapeInputValidator):
    user_data =  await convert_data_to_dict(data)
    stk_ex_links = search_stack_exchange(user_data)
    return stk_ex_links

@scrape_router.post("/vimeo", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_vimeo_profiles(data:ScrapeInputValidator):
    user_data =  await convert_data_to_dict(data)
    vimeo_links = search_vimeo(user_data)
    return vimeo_links

@scrape_router.post("/google-index", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_github_profiles(data:ScrapeInputValidator):
    user_data =  await convert_data_to_dict(data)
    google_index_links = search_indexed_google(user_data)
    return google_index_links