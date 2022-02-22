from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.controller import file_controller, forms_controller

from fastapi import FastAPI


app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(file_controller.router)
app.include_router(forms_controller.router)
