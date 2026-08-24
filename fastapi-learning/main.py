from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from pydantic import Field

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: int
    category: str


class User(BaseModel):
    name: str
    # age: int = Field(gt=0, lt=120)   # gt -> greater than, lt -> less than
    age: int = Field(
        ge=18, le=60
    )  # ge -> greater than equal to, le -> less than equal to
    address: str


@app.get("/")
def users():
    return {"users": [{"id": 1, "name": "Ashutosh"}, {"id": 2, "name": "Alisha"}]}


products = [
    {"id": 1, "name": "Laptop 1", "price": 50000},
    {"id": 2, "name": "Laptop 2", "price": 51000},
    {"id": 3, "name": "Laptop 3", "price": 52000},
    {"id": 4, "name": "Laptop 4", "price": 53000},
    {"id": 5, "name": "Laptop 5", "price": 54000},
    {"id": 6, "name": "Laptop 6", "price": 55000},
    {"id": 7, "name": "Laptop 7", "price": 56000},
    {"id": 8, "name": "Laptop 8", "price": 57000},
    {"id": 9, "name": "Laptop 9", "price": 58000},
    {"id": 10, "name": "Laptop 10", "price": 59000},
]


@app.get("/products")
def get_prdoucts(category_id: str | None = None, limit: int = 10, page: int = 1):
    start = (page - 1) * limit
    end = start + limit

    result = products[start:end]
    return {"data": result, "limit": limit, "page": page}


# Add Product
@app.post("/products")
def create_product(product: Product):

    newProduct = {"id": product.id, "name": product.name, "price": product.price}

    products.append(newProduct)
    return {"message": "Product Created Successfully", "product": newProduct}


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "name": user.name,
        "age": user.age,
        "address": user.address,
    }


# getting product by id
@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return "Product Not Found or Id is not exist"


# updating product by id
@app.put("/products")
def update_product_by_id(id: int, product: Product):
    for i in range(len(products)):
        print("---", products[i], i, products[i]["id"])
        if products[i]["id"] == id:
            products[i] = product
            return "Product updated successfully"
    return "No Product Found"


# delete the product by id
@app.delete("/products")
def delete_product_by_id(id: int):
    for i in range(len(products)):
        if products[i]["id"] == id:
            del products[i]
            return "Product deleted successfully"
    return "No prduct found"


# @app.get("/products/{product_id}")
# def get_product(product_id: int):

#     products = [
#         {"id": 11, "name": "Victus Laptop", "price": 83000},
#         {"id": 12, "name": "Victus Laptop", "price": 83000},
#     ]

#     for item in products:
#         if item["id"] == product_id:
#             return item


# TEST--
productsList = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mobile"},
    {"id": 3, "name": "Keyboard"},
]


def findAll():
    for product in productsList:
        print(product)


def findProductById():
    for i in range(len(productsList)):
        if productsList[i]["id"] == 2:
            print(productsList)
        return "Product Not found"


# HTTPException and 404 Errors
@app.get("/get-product-by-id")
def get_product_by_id(id: int):
    for prod in products:
        if prod["id"] == id:
            return prod

    raise HTTPException(status_code=404, detail="Prdocut not found")
