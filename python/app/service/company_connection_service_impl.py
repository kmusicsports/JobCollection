from werkzeug.datastructures.structures import ImmutableMultiDict

from .company_connection_service import CompanyConnectionService
from app.entity.company_connection import CompanyConnection
from app.repository.company_connection_repository import (
    CompanyConnectionRepository
)
from app.view_model.company_connection_form import CompanyConnectionForm

REQUIRED_KEYS = {
    "company_id",
    "connection_date",
    "way",
    "employee",
    "content",
    "route"
}


class CompanyConnectionServiceImpl(CompanyConnectionService):

    def __init__(
        self, connection_repository: CompanyConnectionRepository
    ):
        self.connection_repository = connection_repository

    def create(
        self, form: ImmutableMultiDict[str, str]
    ) -> CompanyConnectionForm | None:

        required_keys_are_exist = form.keys() >= REQUIRED_KEYS

        if not required_keys_are_exist:
            print("Error: required keys are not exist")
            return None

        company_connection: CompanyConnection = CompanyConnectionForm(
            company_id=form["company_id"],
            connection_date=form["connection_date"],
            way=form["way"],
            employee=form["employee"],
            content=form["content"],
            route=form["route"]
        ).to_entity()
        company_connection = self.connection_repository.save(
            company_connection
        )

        if company_connection:
            return CompanyConnectionForm.from_entity(company_connection)

        return None

    def make_list(self, company_id: int) -> list[CompanyConnectionForm]:
        company_connections = self.connection_repository.find_by_company_id(
            company_id=company_id
        )
        company_connection_forms: list[CompanyConnectionForm] = []

        for company_connection in company_connections:
            company_connection_forms.append(
                CompanyConnectionForm.from_entity(company_connection)
            )

        return company_connection_forms

    def find(self, id: int) -> CompanyConnectionForm | None:
        company_connection = self.connection_repository.find_by_id(id)

        if company_connection:
            return CompanyConnectionForm.from_entity(company_connection)

        return None

    def update(
        self, form: ImmutableMultiDict[str, str]
    ) -> CompanyConnectionForm | None:
        if "id" not in form:
            print("Error: id is not exist")
            return None

        company_connection = self.connection_repository.find_by_id(form["id"])

        if not company_connection:
            print("Error: company_connection is not exist")
            return None

        required_keys_are_exist = form.keys() >= REQUIRED_KEYS

        if not required_keys_are_exist:
            print("Error: required keys are not exist")
            return None

        company_connection: CompanyConnection = CompanyConnectionForm(
            id=form["id"],
            company_id=form["company_id"],
            connection_date=form["connection_date"],
            way=form["way"],
            employee=form["employee"],
            content=form["content"],
            route=form["route"]
        ).to_entity()

        deleted = self.connection_repository.delete_by_id(form["id"])

        if not deleted:
            print("Error: company_connection was not deleted")
            return None

        company_connection = self.connection_repository.save(
            company_connection
        )

        if company_connection:
            return CompanyConnectionForm.from_entity(company_connection)

        return None

    def delete(self, id: int) -> bool:
        deleted = self.connection_repository.delete_by_id(id)
        return deleted
