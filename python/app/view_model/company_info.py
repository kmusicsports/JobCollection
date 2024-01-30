from app.entity.company import Company


class CompanyInfo():

    def __init__(self, company: Company | None = None):
        if company:
            self.id = company.get_id()
            self.name = company.get_name()
            self.business = company.get_business()
            self.mvv = company.get_mvv()
            self.required_skill = company.get_required_skill()
            self.location = company.get_location()
            self.benefit = company.get_benefit()
            self.applying_motivation = company.get_applying_motivation()


    def to_entity(self) -> Company:
        return Company(id=self.id, name=self.name)
