from typing import List, Dict
from models.record import Record

FIELD_ALIASES : Dict[str, List[str]] = {
    "employee_id": ["id", "employee_id", "emp_id"],
    "name": ["name", "fullname", "full_name"],
    "department": ["department", "dept", "division"],
    "hourly_rate": ["hourly_rate", "rate", "salary", "wage"],
    "hours_worked": ["hours_worked", "worked_hours", "hours"]
}

class CsvParser:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def _resolve_headers(self, headers: List[str]) -> Dict[str, int]:
        header_map: Dict[str, int] = {}
        lowered_headers: List[str] = [h.strip().lower() for h in headers]

        for internal_field, aliases in FIELD_ALIASES.items():
            for alias in aliases:
                if alias.lower() in lowered_headers:
                    idx: int = lowered_headers.index(alias.lower())
                    header_map[internal_field] = idx
                    break
            else:
                raise ValueError(f"Отсутствует ожидаемое поле: {internal_field}")
        return header_map

    def parse(self) -> List[Record]:
        records: List[Record] = []
        with open(self.filepath, encoding='utf-8') as f:
            lines: List[str] = f.readlines()

        headers: List[str] = [h.strip() for h in lines[0].split(",")]
        header_map: Dict[str, int] = self._resolve_headers(headers)

        for line in lines[1:]:
            values: List[str] = [v.strip() for v in line.strip().split(",")]
            record = Record(
                employee_id=values[header_map["employee_id"]],
                name=values[header_map["name"]],
                department=values[header_map["department"]],
                hourly_rate=float(values[headтипизацияer_map["hourly_rate"]]),
                hours_worked=float(values[header_map["hours_worked"]])
            )
            records.append(record)
        return records
