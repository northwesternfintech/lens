from pathlib import Path

from loguru import logger

from lens.descriptor import load_data_descriptor
from lens.metadata import CURRENT_VERSION, Metadata

METADATA_FILENAME = "metadata.json"


def check_metadata_exists(base_path: Path) -> bool:
    return (base_path / METADATA_FILENAME).exists()


def check_metadata_version_match(base_path: Path) -> bool:
    with open(base_path / METADATA_FILENAME) as f:
        metadata = Metadata.from_json(f.read())
    return metadata.version >= CURRENT_VERSION


def check_file_structure_correct(base_path: Path) -> bool:
    try:
        descriptor = load_data_descriptor(base_path)
    except FileNotFoundError:
        logger.warning("Failed to build data descriptor - missing files.")
        return False
    data_file_counts = set()
    for _, data_container in descriptor.data_paths.items():
        data_file_counts.add(len(data_container.trade_paths))
        data_file_counts.add(len(data_container.depth_paths))

    if len(data_file_counts) != 1:
        logger.warning("Data files are not uniform in counts.")
        return False
    return True
