import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0",
        port=8080,
        reload=True,

        # openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem
        ssl_keyfile="./ssl/key.pem",
        ssl_certfile="./ssl/cert.pem",
    )
