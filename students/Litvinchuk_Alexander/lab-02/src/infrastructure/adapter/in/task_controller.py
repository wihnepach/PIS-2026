from fastapi import APIRouter
from pydantic import BaseModel
from application.port.inbound.create_task_use_case import CreateTaskUseCase

router = APIRouter(prefix="/api/tasks")


class CreateTaskRequest(BaseModel):
    title: str
    description: str | None = None


class CreateTaskResponse(BaseModel):
    taskId: int


def get_task_controller(create_task_use_case: CreateTaskUseCase):
    @router.post("", response_model=CreateTaskResponse)
    def create_task(request: CreateTaskRequest):
        task_id = create_task_use_case.create(request)
        return CreateTaskResponse(taskId=task_id)

    return router
