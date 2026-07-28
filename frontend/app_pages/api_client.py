import os
import requests


API_BASE_URL = os.getenv("TASKFLOW_API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")


def get_data(path: str):
    response = requests.get(f"{API_BASE_URL}{path}", timeout=5)
    response.raise_for_status()
    return response.json()