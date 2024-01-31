from werkzeug.datastructures.structures import ImmutableMultiDict

from .company_service import CompanyService
from app.entity.company import Company
from app.view_model.company_name import CompanyName
from app.repository.company_repository import CompanyRepository


class CompanyServiceImpl(CompanyService):

    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository

    def create(self, form: ImmutableMultiDict[str, str]) -> CompanyName | None:
        if "name" not in form:
            print("Error: name is not exist")
            return None

        company: Company = CompanyName(name=form["name"]).to_entity()
        company = self.company_repository.save(company)

        if company:
            return CompanyName.from_entity(company)

        return None

    def make_list(self) -> list[CompanyName]:
        companies: list[Company] = self.company_repository.find_all()
        companies_name: list[CompanyName] = []

        for company in companies:
            companies_name.append(CompanyName.from_entity(company))

        return companies_name

    def find(self, id: int) -> CompanyName | None:
        company = self.company_repository.find_by_id(id)

        if company:
            return CompanyName.from_entity(company)

        return None

    def delete(self, id: int) -> bool:
        deleted = self.company_repository.delete_by_id(id)
        return deleted
