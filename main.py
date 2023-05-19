from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    # return 'hey'
    return {"data": {"name": "John"}}

@app.get('/about')
def about():
    return {"data": "about page"}

