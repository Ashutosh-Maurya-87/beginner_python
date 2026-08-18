from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def users():
    return {"users": [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]}


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


# @app.get("/products/{product_id}")
# def get_product(product_id: int):

#     products = [
#         {"id": 11, "name": "Victus Laptop", "price": 83000},
#         {"id": 12, "name": "Victus Laptop", "price": 83000},
#     ]

#     for item in products:
#         if item["id"] == product_id:
#             return item
