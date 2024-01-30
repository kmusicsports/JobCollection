from abc import ABCMeta, abstractmethod
from werkzeug.datastructures.structures import ImmutableMultiDict

from app.view_model.company_connection_form import CompanyConnectionForm


class CompanyConnectionService(metaclass=ABCMeta):

    @abstractmethod
    def create(
        self, form: ImmutableMultiDict[str, str]
    ) -> CompanyConnectionForm | None:
        raise NotImplementedError()

    @abstractmethod
    def make_list(self) -> list[CompanyConnectionForm]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, id: int) -> CompanyConnectionForm | None:
        raise NotImplementedError()

    @abstractmethod
    def update(
        self, form: ImmutableMultiDict[str, str]
    ) -> CompanyConnectionForm | None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError()
