from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from app.core.config import config
from app.api.router import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(
        title=config.app_name,
        debug=config.debug,
        openapi_url=f"{config.api_prefix}/api/openapi.json",
        docs_url=f'{config.api_prefix}/docs',
        redoc_url=f'{config.api_prefix}/redoc',
    )
    origins = ["*"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=config.api_prefix)

    @application.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        err = exc.errors()[0]
        err_msg = f'{err.get("loc")[0]}'
        if len(err.get("loc")) > 2:
            err_msg = f'{err.get("loc")[1]}'
        err_msg += f' {err.get("msg")}'
        return JSONResponse({"detail": err_msg}, status_code=400)

    return application


app = get_application()
