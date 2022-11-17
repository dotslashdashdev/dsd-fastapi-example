from pydantic import BaseModel


class UsersSchema(BaseModel):
    email: str
    status: str
    nickname: str

    class Config:
        orm_mode = True
