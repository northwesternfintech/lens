

from datetime import date

from lens.metadata import Metadata


def test_metadata_to_dict() -> None:
    metadata = Metadata(-1, ["btc"], date.fromisoformat("2025-01-01"), date.fromisoformat("2025-02-01"))
    metadata_dict = metadata.to_dict()
    assert metadata_dict["version"] == -1
    assert metadata_dict["coins"] == ["btc"]
    assert metadata_dict["start"] == "2025-01-01"
    assert metadata_dict["end"] == "2025-02-01"

def test_metadata_serialization_round_trip() -> None:
    metadata = Metadata(-1, ["btc"], date.fromisoformat("2025-01-01"), date.fromisoformat("2025-02-01"))
    json_metadata = metadata.to_json()
    new_metadata = Metadata.from_json(json_metadata)
    assert new_metadata == metadata
