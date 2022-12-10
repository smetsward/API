from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    description: str | None = None


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    surname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    tickets: list[Ticket] = []

    class Config:
        orm_mode = True
