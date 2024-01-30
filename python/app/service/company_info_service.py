from abc import ABCMeta, abstractmethod
from werkzeug.datastructures.structures import ImmutableMultiDict

from app.view_model.company_info import CompanyInfo


class CompanyInfoService(metaclass=ABCMeta):

    @abstractmethod
    def find(self, id: int) -> CompanyInfo | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, form: ImmutableMultiDict[str, str]) -> CompanyInfo | None:
        raise NotImplementedError()
