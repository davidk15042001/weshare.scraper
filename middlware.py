from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response, JSONResponse
from fastapi import Request, status

# MIDDLEWARE
class ScraperMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                content={"error": {"message": f"Error -> {e}"}},
                status_code=status.HTTP_400_BAD_REQUEST
            )