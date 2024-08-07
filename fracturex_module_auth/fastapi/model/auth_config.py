import os
import dotenv
from pydantic import (
    BaseModel, 
    EmailStr,
    StrictStr,
    StrictInt,
    Field
)

from fracturex_module_database.model.database_type import Database_Type

class Database_Config_Tables(BaseModel):
    user : str = None

class Database_Config(BaseModel):
    key_url : str = None
    tables : Database_Config_Tables = None

class Auth_Config(BaseModel):
    database : Database_Config = None

class Auth_PostgreSQL(BaseModel):
    id: StrictInt | None    = Field(title="ID", ge=0)
    data : dict
