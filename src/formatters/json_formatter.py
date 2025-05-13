from formatters.formatter import Formatter
import json
from typing import Dict

class JsonFormatter(Formatter):
    @staticmethod
    def format(data: Dict) -> str:
        return json.dumps(data, indent=4, ensure_ascii=False)
