from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import logging

app = FastAPI()

# Логгирование
logging.basicConfig(level=logging.INFO)

# Модель данных для задачи
class Task(BaseModel):
    chat_id: int
    task_description: str
    delay_seconds: int

@app.post("/task")
async def schedule_task(task: Task):
    logging.info(f"Получена задача: {task.task_description}")
    asyncio.create_task(execute_task(task))
    return {"message": "Задача запланирована!"}

async def execute_task(task: Task):
    await asyncio.sleep(task.delay_seconds)
    logging.info(f"Выполняем задачу: {task.task_description}")
    # Здесь вы можете добавить логику отправки сообщения через Telegram-бот
