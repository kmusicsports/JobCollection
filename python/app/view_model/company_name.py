from __future__ import annotations
from app.entity.company import Company


class CompanyName():

    def __init__(self, id: int | None = None, name: str = ""):
        self.id = id
        self.name = name

    @classmethod
    def from_entity(cls, company: Company) -> CompanyName:
        return cls(
            id=company.get_id(),
            name=company.get_name()
        )

    def to_entity(self) -> Company:
        return Company(id=self.id, name=self.name)

    def get_id(self) -> int:
        return self.id
