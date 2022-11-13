from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, surname=user.surname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(skip).limit(limit).all()


def create_user_ticket(db: Session, ticket: schemas.TicketCreate, user_id: int):
    db_ticket = models.Ticket(**ticket.dict(), owner_id=user_id)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
