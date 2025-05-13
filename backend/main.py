from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def get_products():
    return [
        Product(id=1, name="Қазақи сырға", description="Қолдан жасалған күміс сырға.", price=5000),
        Product(id=2, name="Киіз үй мүсіні", description="Киізден жасалған шағын үй мүсіні.", price=7000),
    ]
