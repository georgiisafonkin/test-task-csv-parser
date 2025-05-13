from abc import ABC, abstractmethod
from typing import Dict

class Formatter(ABC):
    @staticmethod
    @abstractmethod
    def format(data: Dict) -> str:
        pass