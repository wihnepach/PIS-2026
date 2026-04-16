from fastapi import FastAPI

app = FastAPI()

tasks = {}


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    return {"task_id": task_id}