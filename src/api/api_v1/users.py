from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_db
from core.db import crud
from schemas.users import UsersSchema

users_router = APIRouter()


@users_router.get("/users/{user_id}", response_model=UsersSchema)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="찾을 수 없는 사용자 입니다.")
    return db_user
