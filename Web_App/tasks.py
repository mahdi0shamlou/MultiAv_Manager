from fastapi import APIRouter, HTTPException
import requests


# Create an instance of APIRouter
router_tasks = APIRouter(tags=["List Tasks"])

@router_tasks.get("/tasks/list/")
async def status_cape():
    pass

