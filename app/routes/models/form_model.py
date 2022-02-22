from pydantic import BaseModel
from fastapi.param_functions import Body
from typing import Optional


class FormModel(BaseModel):
    first_name: str = None
    second_name: str
