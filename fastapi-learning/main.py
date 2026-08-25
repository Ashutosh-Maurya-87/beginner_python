from fastapi import FastAPI
from products import router as product_router
from users import app as user_router

app = FastAPI()

app.include_router(product_router)
app.include_router(user_router)