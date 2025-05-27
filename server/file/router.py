from fastapi import APIRouter, Request, Depends, HTTPException, Response
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix="/file",
    tags=["file"],
)
