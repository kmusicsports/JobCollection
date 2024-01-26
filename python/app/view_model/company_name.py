from app.entity.company import Company


class CompanyName():

    def __init__(self, company: Company | None = None):
        if company:
            self.id = company.get_id()
            self.name = company.get_name()

    def to_entity(self) -> Company:
        return Company(id=self.id, name=self.name)

    def get_id(self) -> int:
        return self.id
