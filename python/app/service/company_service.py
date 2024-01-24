from abc import ABCMeta, abstractmethod
from werkzeug.datastructures.structures import ImmutableMultiDict

from app.view_model.company_name import CompanyName


class CompanyService(metaclass=ABCMeta):

    @abstractmethod
    def create(self, form: ImmutableMultiDict[str, str]) -> CompanyName | None:
        raise NotImplementedError()

    @abstractmethod
    def make_list(self) -> list[CompanyName]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, id: int) -> CompanyName | None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError()
