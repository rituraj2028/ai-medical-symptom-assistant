from fastapi import Request,HTTPException
from fastapi.responses import JSONResponse

async def global_exception_handler(request:Request,exc:Exception):
    if isinstance(exc,HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success":False,
                "error":exc.detail
            }
        )
    if isinstance(exc,ValueError):
        return JSONResponse(
            status_code = 400,
            content={
                "success":False,
                "error":str(exc)
            }
        )
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error":"Internal Service Error"
        }
    )
