from .company_connection_repository import CompanyConnectionRepository
from app.entity.company_connection import CompanyConnection
from app.database import db


class CompanyConnectionRepositoryImpl(CompanyConnectionRepository):

    def __init__(self):
        pass

    def save(
        self, company_connection: CompanyConnection
    ) -> CompanyConnection | None:
        try:
            db.session.add(company_connection)
            db.session.commit()
        except Exception as e:
            print(e)
            return None

        return company_connection

    def find_by_company_id(self, company_id: int) -> list[CompanyConnection]:
        return CompanyConnection.query.filter_by(
            company_id=company_id).order_by(CompanyConnection.connection_date)

    def find_by_id(self, id: int) -> CompanyConnection | None:
        return CompanyConnection.query.filter_by(id=id).first()

    def delete_by_id(self, id: int) -> bool:
        company_connection = self.find_by_id(id)

        if not company_connection:
            print("Error: company not found")
            return False

        try:
            db.session.delete(company_connection)
            db.session.commit()
        except Exception as e:
            print(e)
            return False

        return True
