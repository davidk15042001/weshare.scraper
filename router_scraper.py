from fastapi import APIRouter, status, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.future import select

from validators import ScrapeInputValidator
from utils import search_github, search_gitlab, search_indexed_google, search_stack_exchange, search_vimeo
from auth import authenticate

from models import GithubScrape, GitlabScrape, GoogleScrape, StackOverflowScrape, VimeoScrape
from database import db_dependency



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
async def get_github_profiles(data:ScrapeInputValidator, db:db_dependency):
    user_data =  await convert_data_to_dict(data)
    FIELD_MAP = {
        "first_name": GithubScrape.first_name,
        "last_name": GithubScrape.last_name,
        "email": GithubScrape.email,
        "phone": GithubScrape.phone,
        "country": GithubScrape.country,
    }
    filters = [
        column == user_data[key]
        for key, column in FIELD_MAP.items()
        if user_data.get(key)
    ]
    stmt = select(GithubScrape).where(*filters)
    result = await db.execute(stmt)
    github_results = result.scalars().all()
    if not github_results:
        github_links = search_github(user_data)
        if github_links:
            github_scrape = [GithubScrape(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                phone=user_data["phone"],
                country=user_data["country"],
                platform=link["platform"],
                title=link["title"],
                link=link["link"],
                avatar_url=link["avatar_url"],
            ) for link in github_links]
            try:
                db.add_all(github_scrape)
                await db.commit()

                for scrape in github_scrape:
                    await db.refresh(scrape)
            except Exception as e:
                return JSONResponse(
                    content={
                        f"ERROR -> {e}"
                    }, status_code=status.HTTP_400_BAD_REQUEST
                )
            return github_scrape
        else:
            return []
    return github_results

@scrape_router.post("/gitlab", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_gitlab_profiles(data:ScrapeInputValidator, db:db_dependency):
    user_data =  await convert_data_to_dict(data)
    gitlab_links = search_gitlab(user_data)
    if gitlab_links:
        gitlab_scrape = [GitlabScrape(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            phone=user_data["phone"],
            country=user_data["country"],
            platform=link["platform"],
            title=link["title"],
            link=link["link"],
            avatar_url=link["avatar_url"],
        ) for link in gitlab_links]
        try:
            db.add_all(gitlab_scrape)
            await db.commit()

            for scrape in gitlab_scrape:
                await db.refresh(scrape)
        except Exception as e:
            return JSONResponse(
                content={
                    f"ERROR -> {e}"
                }, status_code=status.HTTP_400_BAD_REQUEST
            )
        return gitlab_scrape
    return gitlab_links

@scrape_router.post("/stack-overflow", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_stack_overflow_profiles(data:ScrapeInputValidator, db:db_dependency):
    user_data =  await convert_data_to_dict(data)
    stk_ex_links = search_stack_exchange(user_data)
    if stk_ex_links:
        stk_ex_scrape = [StackOverflowScrape(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            phone=user_data["phone"],
            country=user_data["country"],
            platform=link["platform"],
            title=link["title"],
            link=link["link"],
            avatar_url=link["avatar_url"],
        ) for link in stk_ex_links]
        try:
            db.add_all(stk_ex_scrape)
            await db.commit()

            for scrape in stk_ex_scrape:
                await db.refresh(scrape)
        except Exception as e:
            return JSONResponse(
                content={
                    f"ERROR -> {e}"
                }, status_code=status.HTTP_400_BAD_REQUEST
            )
        return stk_ex_scrape
    return stk_ex_links

@scrape_router.post("/vimeo", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_vimeo_profiles(data:ScrapeInputValidator, db:db_dependency):
    user_data =  await convert_data_to_dict(data)
    vimeo_links = search_vimeo(user_data)
    if vimeo_links:
        vimeo_scrape = [VimeoScrape(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            phone=user_data["phone"],
            country=user_data["country"],
            platform=link["platform"],
            title=link["title"],
            link=link["link"],
            avatar_url=link["avatar_url"],
        ) for link in vimeo_links]
        try:
            db.add_all(vimeo_scrape)
            await db.commit()

            for scrape in vimeo_scrape:
                await db.refresh(scrape)
        except Exception as e:
            return JSONResponse(
                content={
                    f"ERROR -> {e}"
                }, status_code=status.HTTP_400_BAD_REQUEST
            )
        return vimeo_scrape
    return vimeo_links

@scrape_router.post("/google-index", dependencies=[Depends(authenticate)], status_code=status.HTTP_200_OK)
async def get_google_index_profiles(data:ScrapeInputValidator, db:db_dependency):
    user_data =  await convert_data_to_dict(data)
    google_index_links = search_indexed_google(user_data)
    if google_index_links:
        google_scrape = [GoogleScrape(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            phone=user_data["phone"],
            country=user_data["country"],
            platform=link["platform"],
            title=link["title"],
            link=link["link"],
            snippet=link["snippet"],
        ) for link in google_index_links]
        try:
            db.add_all(google_scrape)
            await db.commit()

            for scrape in google_scrape:
                await db.refresh(scrape)
        except Exception as e:
            return JSONResponse(
                content={
                    f"ERROR -> {e}"
                }, status_code=status.HTTP_400_BAD_REQUEST
            )
        return google_scrape
    return google_index_links