from pydantic import BaseModel

class ProjectCreate(BaseModel):
      title: str
      content: str

class ProjectUpdate(BaseModel):
      id: str
      title: str
      content: str

class ProjectGet(BaseModel):
    id: str
    title: str   
    content: str
    created_at: str
