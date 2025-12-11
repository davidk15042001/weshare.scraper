from fastapi import HTTPException, status, Security
from fastapi.security.api_key import APIKeyHeader
from decouple import config


api_key_header = APIKeyHeader(name="X-API-Key")

async def authenticate(api_key_header: str = Security(api_key_header)):
    if api_key_header == config("API_KEY"):
        return api_key_header   
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )