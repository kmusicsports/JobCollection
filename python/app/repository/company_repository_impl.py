from .company_repository import CompanyRepository
from app.entity.company import Company
from app.database import db


class CompanyRepositoryImpl(CompanyRepository):

    def __init__(self):
        pass

    def save(self, company: Company) -> Company | None:
        try:
            db.session.add(company)
            db.session.commit()
        except Exception as e:
            print(e)
            return None

        return company

    def find_all(self) -> list[Company]:
        return Company.query.all()

    def find_by_id(self, id: int) -> Company | None:
        return Company.query.filter_by(id=id).first()

    def delete_by_id(self, id: int) -> bool:
        company = self.find_by_id(id)

        if not company:
            print("Error: company not found")
            return False

        try:
            db.session.delete(company)
            db.session.commit()
        except Exception as e:
            print(e)
            return False

        return True
