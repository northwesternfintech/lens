import json
from dataclasses import asdict, dataclass
from datetime import date

CURRENT_VERSION = 0


@dataclass
class Metadata:
    version: int
    coins: list[str]
    start: date
    end: date

    def to_dict(self) -> dict:
        data = asdict(self)
        data["start"] = self.start.isoformat()
        data["end"] = self.end.isoformat()
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    @classmethod
    def from_json(cls, json_str: str) -> "Metadata":
        data = json.loads(json_str)
        data["start"] = date.fromisoformat(data["start"])
        data["end"] = date.fromisoformat(data["end"])
        return cls(**data)
