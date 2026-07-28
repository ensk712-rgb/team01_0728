from dotenv import load_dotenv
from fastapi import FastAPI

from routers.task_router import 

load_dotenv()
app = FastAPI(title="TaskFlow API", version="0.1.0")
app.include_router()
app.include_router()
