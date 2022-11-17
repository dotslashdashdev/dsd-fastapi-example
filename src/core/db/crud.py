from sqlalchemy.orm import Session

from . import models


def get_user(db: Session, user_id: str):
    return (
        db.query(models.Users)
        .filter(models.Users.id == user_id, models.Users.status == "activation")
        .first()
    )
