from fastapi import FastAPI
from models import Product
from database import products

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "KazArtisans API"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product added successfully"}
