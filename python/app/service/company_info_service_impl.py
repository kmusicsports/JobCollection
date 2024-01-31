from werkzeug.datastructures.structures import ImmutableMultiDict

from app.entity.company import Company
from app.view_model.company_info import CompanyInfo
from .company_info_service import CompanyInfoService
from app.repository.company_repository import CompanyRepository

REQUIRED_KEYS = {
    "id",
    "name",
    "business",
    "mvv",
    "required_skill",
    "location",
    "benefit",
    "applying_motivation"
}

class CompanyInfoServiceImpl(CompanyInfoService):

    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository


    def update(self, form: ImmutableMultiDict[str, str]) -> CompanyInfo | None:
        required_keys_are_exist = form.keys() >= REQUIRED_KEYS

        if not required_keys_are_exist:
            print("Error: required keys are not exist")
            return None

        company = self.company_repository.find_by_id(id=form["id"])

        if not company:
            print("Error: company is not exist")
            return None

        deleted = self.company_repository.delete_by_id(id=form["id"])

        if not deleted:
            print("Error: company was not deleted")
            return None

        company = Company(
            id=form["id"],
            name=form["name"],
            business=form["business"],
            mvv=form["mvv"],
            required_skill=form["required_skill"],
            location=form["location"],
            benefit=form["benefit"],
            applying_motivation=form["applying_motivation"]
        )

        company = self.company_repository.save(company)

        if company:
            return CompanyInfo(company)

        return None

    def find(self, id: int) -> CompanyInfo | None:
        company = self.company_repository.find_by_id(id)

        if company:
            return CompanyInfo(company)

        return None
