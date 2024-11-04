from app.models import Task
#from fastapi_filters import Filter
from pydantic import Field
from typing import Optional
from app.core.constants import Status


class TaskFilter(Filter):
    name__in: Optional[list[str]] = Field(alias="names")
    status_in: Optional[list[Status]] = Field(alias="types")

    class Constants(Filter.Constants):
        model = Task

    class Config:
        allow_population_by_field_name = True
