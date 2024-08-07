from fastapi import (
    status
)
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from psycopg2.extensions import connection

from fracturex_module_database.model.dto.http_response import HTTP_Response
from src.shared.models.response import messages
from src.shared.utils.functions.functions import validate_user
from src.shared.utils.functions.functions import to_json

async def login(form_data: OAuth2PasswordRequestForm, connPostgreSQL: connection) -> dict | JSONResponse:
    try:
        # Validar que venga la data
        HTTP_Response()
        if (not form_data.username or not form_data.password): return getJsonResponse(headers={"WWW-Authenticate": "Bearer"}, status_code=status.HTTP_401_UNAUTHORIZED, success=False, message=messages.CREDENTIALS_COULD_NOT_VALIDATE)
        
        result = await validate_user(form_data=form_data, connPostgreSQL=connPostgreSQL)
        if isinstance(result, JSONResponse): return result
        
        return getJsonResponse(
            headers={
                "WWW-Authenticate": "Bearer"
            }, 
            status_code=status.HTTP_200_OK, 
            success=True,
            message="",
            data=to_json(object=result)
        )
    except Exception as e:
        return getJsonResponse(headers={"WWW-Authenticate": "Bearer"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, success=False, message=f"There was an error: {str(e)}", data={})
