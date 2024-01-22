from app.entity.company import Company


class CompanyName():

    def __init__(self, company: Company | None = None):
        if company:
            self.id = company.id
            self.name = company.name

    def to_entity(self) -> Company:
        return Company(id=self.id, name=self.name)
