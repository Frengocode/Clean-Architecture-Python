from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.application.common.shared.database.sqlalchemy.mixins import BaseMixin
from src.application.common.shared.database.sqlalchemy.sqlalchemy_database import Base


class User(Base, BaseMixin):

    username: Mapped[str] = mapped_column(String(30), index=True)
    email: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[str] = mapped_column(String)
