from werkzeug.datastructures.structures import ImmutableMultiDict

from app.entity.company import Company
from app.view_model.company_info import CompanyInfo
from .company_info_service import CompanyInfoService
from app.repository.company_repository import CompanyRepository


class CompanyInfoServiceImpl(CompanyInfoService):

    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository


    def update(self, form: ImmutableMultiDict[str, str]) -> CompanyInfo | None:
        if "business" not in form:
            return False
        #campanyに各種変数を入れてsave
        company = Company(business=form["business"])
        company = Company(mvv=form["mvv"])
        company = Company(required_skill=form["required_skill"])
        company = Company(location=form["location"])
        company = Company(benefit=form["benefit"])
        company = Company(applying_motivation=form["applying_motivation"])
        company = self.company_repository.save(company)

        if company:
            return CompanyInfo(company)

        return None

    def find(self, id: int) -> CompanyInfo | None:
        company = self.company_repository.find_by_id(id)

        if company:
            return CompanyInfo(company)

        return None
