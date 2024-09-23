from fastapi import FastAPI





app = FastAPI(
    title='Test Kĩ Năng Backend',
)

 


@app.get("/")
async def root():
    return {"message": "Hello World"}
