from abc import ABC, abstractmethod
from typing import List, Dict
from models.record import Record

class Report(ABC):
    def __init__(self, records: List[Record]):
        self.records = records

    @abstractmethod
    def generate(self) -> Dict:
        pass
