from abc import ABCMeta, abstractmethod

from app.entity.company import Company


class CompanyRepository(metaclass=ABCMeta):

    @abstractmethod
    def save(self, company: Company) -> Company | None:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self) -> list[Company]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id: int) -> Company | None:
        raise NotImplementedError()

    @abstractmethod
    def delete_by_id(self, id: int) -> bool:
        raise NotImplementedError()
