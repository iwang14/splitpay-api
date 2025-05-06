from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SplitPay API is running"}

    