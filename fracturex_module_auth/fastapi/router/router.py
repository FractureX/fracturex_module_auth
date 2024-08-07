from fastapi import (
    APIRouter, 
    Depends
)
from fastapi.security import OAuth2PasswordRequestForm

from fracturex_module_database.service import service as database_service
from fracturex_module_auth.fastapi.config.environment import environment
from fracturex_module_auth.fastapi.service import service

router = APIRouter(prefix = "/login")

@router.post("/", name = "Login and get access token")
async def login(form_data : OAuth2PasswordRequestForm = Depends(), conn = Depends(lambda: database_service.get_database_connection(environment.FRACTUREX_MODULE_AUTH_CONFIG.database.key_url))):
    result = await service.login(form_data = form_data, connPostgreSQL = conn)
    return result
