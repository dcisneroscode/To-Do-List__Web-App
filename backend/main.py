# My imports
from database.database import Base, engine
from router.user_router import router_user_path
from router.task_router import router_task_path
from router.login_router import router_login_path
from middleware.cors_middleware import origins
from middleware.error_middleware import Error_Handler


# FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.title= "Task Manager App"
app.version= "0.0.1"
app.include_router(router_user_path)
app.include_router(router_task_path)
app.include_router(router_login_path)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(Error_Handler)

