from fastapi import FastAPI

app = FastAPI()

"""  uvicorn app.main:app --reload use this to load this  
now when you go to http://127.0.0.1:8000/(the app.get() values you can access the api) 

example: http://127.0.0.1:8000/test_case/1
"""


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI wizard!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"Hello, {name}!"}
@app.get("/test_case/{value}")
def test(value : int):
    return {'warning 1': f'{value}This works'}