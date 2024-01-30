from __future__ import annotations
from datetime import date

from app.entity.company_connection import CompanyConnection


class CompanyConnectionForm():

    def __init__(
        self,
        id: int | None = None,
        company_id: int = -1,
        connection_date: str = "",
        way: str | None = None,
        employee: str | None = None,
        content: str = "",
        route: str | None = None
    ):
        self.id = id
        self.company_id = company_id
        self.connection_date = connection_date
        self.way = way
        self.employee = employee
        self.content = content
        self.route = route

    @classmethod
    def from_entity(
        cls, company_connection: CompanyConnection
    ) -> CompanyConnectionForm:
        connection_date = company_connection.get_connection_date()

        if type(connection_date) is date:
            connection_date: str = connection_date.strftime('%Y-%m-%d')

        return cls(
            id=company_connection.get_id(),
            company_id=company_connection.get_company_id(),
            connection_date=connection_date,
            way=company_connection.get_way(),
            employee=company_connection.get_employee(),
            content=company_connection.get_content(),
            route=company_connection.get_route()
        )

    def to_entity(self) -> CompanyConnection:
        return CompanyConnection(
            id=self.id,
            company_id=self.company_id,
            connection_date=self.connection_date,
            way=self.way,
            employee=self.employee,
            content=self.content,
            route=self.route
        )
