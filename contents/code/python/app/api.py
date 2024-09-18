from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1")
def hello_world():
    return "Hello World"
