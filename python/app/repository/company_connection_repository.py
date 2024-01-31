from abc import ABCMeta, abstractmethod

from app.entity.company_connection import CompanyConnection


class CompanyConnectionRepository(metaclass=ABCMeta):

    @abstractmethod
    def save(
        self, company_connection: CompanyConnection
    ) -> CompanyConnection | None:
        raise NotImplementedError()

    @abstractmethod
    def find_by_company_id(self, company_id: int) -> list[CompanyConnection]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id: int) -> CompanyConnection | None:
        raise NotImplementedError()

    @abstractmethod
    def delete_by_id(self, id: int) -> bool:
        raise NotImplementedError()
