from sqlalchemy.orm import Session

from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryRead, CategoryCreate, CategoryUpdate

	
class CategoryNotFoundError(Exception):
    pass

class CategoryService:
    """Ключевые операции с задачами, включая бизнес-логику, валидацию и прочее"""

    def __init__(self, db: Session):
        self.db = db
        self.repository = CategoryRepository(db)

    def list_categories(self) -> list[CategoryRead]:
        categories = self.repository.get_all()
        return [CategoryRead.model_validate(category) for category in categories] # список Pydantic моделей

    def create_category(self, payload: CategoryCreate) -> CategoryRead:
        category = self.repository.create(name=payload.name)
        self.db.commit()
        return CategoryRead.model_validate(category)

    def update_category(self, category_id: str, payload: CategoryUpdate) -> CategoryRead:
        category = self.repository.get_by_id(category_id)

        if payload.name is not None:
            category.name = payload.name

        self.db.commit()
        return CategoryRead.model_validate(category)

    def delete_category(self, category_id: str) -> None:
        category = self.repository.get_by_id(category_id)

        self.repository.delete(category)
        self.db.commit()