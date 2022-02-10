from __future__ import annotations
from fastapi import APIRouter, Depends, Query
from app.routes.service import file_service
from typing import Optional, List
from pydantic import SecretStr


router = APIRouter(prefix="/api")


@router.get("/health", tags=["Health Check"])
async def health_endpoint():
    return file_service.test_health()


@router.get("/user-details", tags=["User Details"])
async def get_user_details(username: str,
                           password: SecretStr):
    password = password.get_secret_value()
    return file_service.user_details(username, password)


@router.get("/file-details", tags=["File Operations"])
async def get_file_details(username: str,
                           password: SecretStr,
                           repository_name: str,
                           file_path: Optional[str] = None):
    password = password.get_secret_value()
    return file_service.file_details(username, password, repository_name, file_path)
