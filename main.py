# from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi // import fastapi

# appTest = FastAPI() # gọi constructor và gán vào biến app  // tạo 1 instance của class FastAPI
# # uvicorn main:appTest --host 0.0.0.0 --port 8000



# @appTest.get("/") # giống flask, khai báo phương thức get và url // tạo đường dẫn, bắt đầu từ / // khai báo phương thức HTTP: post, get, put, delete hay options, head, patch, trace
# async def test(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi // khai báo hàm
#     return {"message Test": "Hello"} # // trả về content với format dict, list, str, int, ...


# @appTest.get("/items/{item_id}") # khai báo đường dẫn có tham số // khai báo đường dẫn có tham số   
# async def read_item(item_id: int): # khai báo hàm với tham số item_id có kiểu dữ liệu là int
#     return {"item_id": item_id} # trả về content với format dict, list, str, int, ...

# # Query Parameters
# fake_items_db = [
#     {"item_name": "Foo"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Bar"}, 
#     {"item_name": "Ba3"}, 
#     {"item_name": "Ba4"}, 
#     {"item_name": "Baz"}] # pair format: key-value


# @appTest.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit] # trả về dữ liệu từ skip đến skip + limit
from typing import List, Optional

from fastapi import FastAPI, Query

appTest = FastAPI()


@appTest.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

