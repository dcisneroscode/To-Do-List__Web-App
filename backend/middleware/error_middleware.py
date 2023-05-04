# Starlette imports
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

# FastAPI imports
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse





class Error_Handler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response or JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})