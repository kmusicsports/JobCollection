from __future__ import annotations
from datetime import date

from sqlalchemy import Column, Integer, Date, Text, ForeignKey

from app.database import db


class CompanyConnection(db.Model):
    __tablename__ = 'company_connection'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(
        Integer, ForeignKey('company.id'), nullable=False
    )
    connection_date = Column(Date, nullable=False)
    way = Column(Text)
    employee = Column(Text)
    content = Column(Text, nullable=False)
    route = Column(Text)

    def __init__(
        self,
        id: int | None = None,
        company_id: int = -1,
        connection_date: date = date.today(),
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

    def get_id(self) -> int:
        return self.id

    def get_company_id(self) -> int:
        return self.company_id

    def get_connection_date(self) -> date:
        return self.connection_date

    def get_way(self) -> str:
        return self.way

    def get_employee(self) -> str:
        return self.employee

    def get_content(self) -> str:
        return self.content

    def get_route(self) -> str:
        return self.route
