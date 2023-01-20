from settings import Settings, get_settings
from fastapi import Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN

api_key_query = APIKeyQuery(name="api_key", auto_error=False)

async def get_api_key(settings: Settings = Depends(get_settings), api_key_query: str = Security(api_key_query)):
    if api_key_query == settings.API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Invalid API key"
        )