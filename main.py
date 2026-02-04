from fastapi import FastAPI
import database_models
from models import product
from database import session,engine
app=FastAPI()

database_models.base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, World!"

products=[
    product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    product(id=2, name="Smartphone", description="A latest model smartphone", price=599.99, quantity=20),
    product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15) 
]

def inti_db():
    db=session()
    count =db.query(database_models.Product).count()
    if count==0:
        for prod in products:
            db.add(database_models.Product(**prod.model_dump()))
        db.commit()
inti_db()
@app.get("/products")
def get_products():
    db=session()
    db_products=db.query(database_models.Product).all()
    return {"products": db_products}

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