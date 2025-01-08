from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
async def root():
    return {"message": "Time Sleep Action Service is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
