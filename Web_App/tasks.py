from lib import Make_URL
from fastapi import APIRouter, File, UploadFile, HTTPException
import requests
import base64
from typing import Optional

# Create an instance of APIRouter
router_tasks = APIRouter(tags=["List Tasks"])

@router_tasks.get("/tasks/list/")
async def task_lists():
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
        raise HTTPException(status_code=500, detail=str(e))

@router_tasks.get("/tasks/details/{task_id}")
async def task_details(task_id: int):
    try:
        additional_url = f"/api/v1/sample/{task_id}"
        requests_url = Make_URL.MakeUrl.get_url_address(additional_url)
        response = requests.get(requests_url)
        response.raise_for_status()  # Raise an error for bad responses

        return_dicts = {
            "status" : "okay",
            "data" : response.json()
        }
        return return_dicts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@router_tasks.post("/tasks/submit/")
async def task_details(
    allow_internet: bool,
    minspeed: int,
    sample_file: UploadFile = File(...),
    sample_name: Optional[str] = None
):
    try:
        # Read the uploaded file and encode it in Base64
        file_contents = await sample_file.read()

        encoded_sample = base64.b64encode(file_contents)


        # Prepare the additional URL for the request
        additional_url = f"/api/v1/sample"  # Adjust as necessary
        requests_url = Make_URL.MakeUrl.get_url_address(additional_url)

        # Prepare the payload for the POST request
        payload = {
            "allow_internet": "true" if allow_internet else "false",
            "minspeed": minspeed,
            "sample": str(encoded_sample),
            "sample_name": sample_name
        }

        response = requests.post(requests_url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses

        return_dicts = {
            "status": "okay",
            "data": response.json()
        }
        return return_dicts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

