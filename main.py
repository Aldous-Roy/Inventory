from fastapi import FastAPI
from models import product
app=FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products=[
    product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    product(id=2, name="Smartphone", description="A latest model smartphone", price=599.99, quantity=20)
]
@app.get("/products")
def get_products():
    return {"products": products}