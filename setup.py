import os
from dotenv import load_dotenv
from setuptools import setup, find_packages

# Cargar valores del .env
load_dotenv()

setup(
    name = "fracturex-module-auth-fastapi",
    version = "1.0.0",
    packages = find_packages(),
    install_requires = [
        f"fracturex-module-database @ git+https://{os.getenv('FRACTUREX_MODULE_GITHUB_TOKEN')}:x-oauth-basic@github.com/FractureX/fracturex-module-database.git"
    ],
    author = "FractureX",
    author_email = "shaquille.montero.vergel123@example.com",
    description = "Módulo de autenticación usando FastAPI",
    url = "https://github.com/FractureX/fracturex-module-auth-fastapi"
)