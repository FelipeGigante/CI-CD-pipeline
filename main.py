from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def __main__():
    return "Olá Mundo"