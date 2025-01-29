from fastapi import APIRouter, HTTPException
import requests
from lib import Make_URL





# Create an instance of APIRouter
router_tasks = APIRouter(tags=["List Tasks"])

@router_tasks.get("/tasks/list/")
async def status_cape():
    try:

        additional_url = "/api/v1/sample"
        requests_url = Make_URL.MakeUrl.get_url_address(additional_url)
        response = requests.get(requests_url)
        response.raise_for_status()  # Raise an error for bad responses

        return_dicts = {
            "status" : "okay",
            "data" : response.json()
        }
        return return_dicts

    except Exception as e:
        return_dicts = {
            "error": f"{e}"
        }
        return return_dicts
