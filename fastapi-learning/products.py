from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

router = APIRouter()

productsData = [
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


class Product(BaseModel):
    id: int
    name: str
    price: int
    category: str


@router.get("/products")
def get_prdoucts(category_id: str | None = None, limit: int = 10, page: int = 1):
    start = (page - 1) * limit
    end = start + limit

    result = productsData[start:end]
    return {"data": result, "limit": limit, "page": page}


# Add Product
@router.post("/products")
def create_product(product: Product):

    newProduct = {"id": product.id, "name": product.name, "price": product.price}

    productsData.append(newProduct)
    return {"message": "Product Created Successfully", "product": newProduct}


# getting product by id
@router.get("/products/{id}")
def get_product_by_id(id: int):
    for product in productsData:
        if product["id"] == id:
            return product
    return "Product Not Found or Id is not exist"


# updating product by id
@router.put("/products")
def update_product_by_id(id: int, product: Product):
    for i in range(len(productsData)):
        print("---", productsData[i], i, productsData[i]["id"])
        if productsData[i]["id"] == id:
            productsData[i] = product
            return "Product updated successfully"
    return "No Product Found"


# delete the product by id
@router.delete("/products")
def delete_product_by_id(id: int):
    for i in range(len(productsData)):
        if productsData[i]["id"] == id:
            del productsData[i]
            return "Product deleted successfully"
    return "No prduct found"


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
@router.get("/get-product-by-id")
def get_product_by_id(id: int):
    for prod in productsData:
        if prod["id"] == id:
            return prod

    raise HTTPException(status_code=404, detail="Prdocut not found")
