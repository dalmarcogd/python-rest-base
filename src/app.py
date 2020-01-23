from fastapi import FastAPI

from src.handlers.health_check import health_check_router
from src.settings import DEBUG, BASE_PATH

app = FastAPI(debug=DEBUG)
app.include_router(health_check_router, prefix=BASE_PATH)
