from app.entity.company import Company


class CompanyInfo():

    def __init__(self, company: Company | None = None):
        if company:
            self.id = company.get_id()
            self.name = company.get_name()
            self.business = '' if company.get_business() is None else company.get_business()
            self.mvv = '' if company.get_mvv() is None else company.get_mvv()
            self.required_skill = '' if company.get_required_skill() is None else company.get_required_skill()
            self.location = '' if company.get_location() is None else company.get_location()
            self.benefit = '' if company.get_benefit() is None else company.get_benefit()
            self.applying_motivation = '' if company.get_applying_motivation() is None else company.get_applying_motivation()

    def to_entity(self) -> Company:
        return Company(
            id=self.id,
            name=self.name,
            business=self.business,
            mvv=self.mvv,
            required_skill=self.required_skill,
            location=self.location,
            benefit=self.benefit,
            applying_motivation=self.applying_motivation
        )
