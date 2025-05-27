from fastapi import APIRouter, Request, Depends, HTTPException, Response
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix="/user",
    tags=["user"],
)
