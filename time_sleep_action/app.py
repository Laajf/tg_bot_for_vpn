from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
scheduler = BackgroundScheduler()

@app.on_event("startup")
def startup_event():
    scheduler.start()

@app.get("/schedule_task/{minutes}")
def schedule_task(minutes: int):
    scheduler.add_job(my_task, 'interval', minutes=minutes)
    return {"message": f"Task scheduled to run every {minutes} minutes"}

def my_task():
    print("Task executed!")
