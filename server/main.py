from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from direction.router import router as direction_router
from file.router import router as file_router
from user.router import router as user_router


app = FastAPI()

app.include_router(direction_router, prefix="/api")
app.include_router(file_router, prefix="/api")
app.include_router(user_router, prefix="/api")


@app.get("/api")
def index():
    return RedirectResponse(url="/api/status")
@app.get("/api/status")
def read_status():
    return {"status": "ok"}


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://shap.software",
    "http://87.252.252.226:3333",
    "http://192.168.1.100"
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)