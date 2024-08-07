import os
import json
from dotenv import load_dotenv

from fracturex_module_auth.fastapi.model.auth_config import Auth_Config

# Cargar variables de entorno
load_dotenv()

class Environment:
    FRACTUREX_MODULE_AUTH_CONFIG : Auth_Config = Auth_Config(**json.loads(os.getenv("FRACTUREX_MODULE_AUTH_CONFIG")))

# Valores extraídos del .env
environment : Environment = Environment()
