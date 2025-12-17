from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

from router_scraper import scrape_router
from middlware import ScraperMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8022"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    # Grab the first missing field error only
    for error in exc.errors():
        if error["type"] == "value_error.missing":
            field = error["loc"][-1]

            return JSONResponse(
                status_code=400,
                content={
                    "error": f"missing {field}",
                    "message": f"please provide {field}"
                },
            )

    # Fallback if some other validation happens
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid request",
            "message": "request validation failed"
        }
    )


@app.get("/test")
async def api_test():
    return {
        "message":"API is Working!"
    }

app.include_router(scrape_router)
app.add_middleware(ScraperMiddleware)

if __name__=="__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)