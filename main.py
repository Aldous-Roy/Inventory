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

@app.get("/products/{id}")
def get_Product_by_id(id:int):
    for product in products:
        if product.id==id:
            return {"product": product}
    return {"message": "Product not found"}

@app.post("/products")
def add_product(new_product: product):
    products.append(new_product)
    return {"message": "Product added successfully", "product": new_product}

@app.put("/products/{id}")
def update_product(id:int, updated_product: product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    return {"message": "Product not found"}


@app.delete("/products/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            deleted_product=products.pop(i)
            return {"message": "Product deleted successfully", "product": deleted_product}
    return {"message": "Product not found"}