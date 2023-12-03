from abc import ABC, abstractmethod
from typing import Callable, TypeVar


T = TypeVar("T", bound="InterfaceSQL")


class InterfaceSQL(ABC):
    def make_stmt(self, sql_name: str, /, *args, **kwargs):
        func_query: Callable = self.lookup_query(sql_name)
        return func_query(*args, **kwargs)

    @abstractmethod
    def lookup_query(self, sql_name: str) -> Callable:
        pass
