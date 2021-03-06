import datetime as dt

from flask_login import UserMixin
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    orm,
    Boolean,
)
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class Order(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=True)
    created_datetime = Column(DateTime, default=dt.datetime.now)
    owner_email = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    is_fulfilled = Column(Boolean, default=False)
    is_used = Column(Boolean, default=False)
    is_declined = Column(Boolean, default=False)
    event = orm.relationship("Event", back_populates="orders")
    owner = orm.relationship("User", back_populates="orders", lazy="subquery")

    def __repr__(self):
        return (
            f"<Order> {self.id}: {self.event_id} (Event),"
            f"{self.owner_email} (Owner)"
        )
