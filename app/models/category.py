from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class CategoryORM(Base):
    """Модель категории в БД"""

    __tablename__ = "categories"

    name: Mapped[str]