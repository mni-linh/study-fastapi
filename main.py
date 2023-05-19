from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi // import fastapi

appTest = FastAPI() # gọi constructor và gán vào biến app  // tạo 1 instance của class FastAPI


@appTest.get("/") # giống flask, khai báo phương thức get và url // tạo đường dẫn, bắt đầu từ / // khai báo phương thức HTTP: post, get, put, delete hay options, head, patch, trace
async def test(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi // khai báo hàm
    return {"message": "Hello Worldd 2"} # // trả về content với format dict, list, str, int, ...


@appTest.get("/items/{item_id}") # khai báo đường dẫn có tham số // khai báo đường dẫn có tham số   
async def read_item(item_id: int): # khai báo hàm với tham số item_id có kiểu dữ liệu là int // khai báo hàm với tham số item_id có kiểu dữ liệu là int
    return {"item_id": item_id} # trả về content với format dict, list, str, int, ...