# My imports
from database.database import Base, engine
from router.user_router import router_user_path
from router.task_router import router_task_path


# FastAPI imports
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.title= "Task Manager App"
app.version= "0.0.1"
app.include_router(router_user_path)
app.include_router(router_task_path)
