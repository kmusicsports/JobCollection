from werkzeug.datastructures.structures import ImmutableMultiDict

from app.entity.company import Company
from app.view_model.company_name import CompanyName
from .company_service import CompanyService
from app.repository.company_repository import CompanyRepository


class CompanyServiceImpl(CompanyService):

    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository

    def create(self, form: ImmutableMultiDict[str, str]) -> CompanyName | None:
        if "companyName" not in form:
            return False

        print(type(form))
        company = Company(name=form["companyName"])
        company = self.company_repository.save(company)

        if company:
            return CompanyName(company)

        return None

    def make_list(self) -> list[CompanyName]:
        companies: list[Company] = self.company_repository.find_all()
        companies_name = [CompanyName(company) for company in companies]
        return companies_name

    def find(self, id: int) -> CompanyName | None:
        company = self.company_repository.find_by_id(id)

        if company:
            return CompanyName(company)

        return None

    def delete(self, id: int) -> bool:
        deleted = self.company_repository.delete_by_id(id)
        return deleted
