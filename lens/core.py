from pathlib import Path

from loguru import logger

from lens.util.hostname import check_valid_lens_hostname, get_hostname
from lens.util.paths import check_file_structure_correct, check_metadata_exists, check_metadata_version_match


class Lens:
    def __init__(self) -> None:
        pass

    def startup(self, data_root: Path) -> None:
        if not check_valid_lens_hostname(get_hostname()):
            raise RuntimeError("Cannot start lens on invalid host.")
        logger.info("Host check succeeded.")
        if not check_metadata_exists(data_root):
            raise RuntimeError("Failed to find metadata.json file in the data directory.")
        logger.info("Metadata found.")
        if not check_metadata_version_match(data_root):
            raise RuntimeError("Metadata version does not match current version!")
        logger.info("Metadata versions match.")
        if not check_file_structure_correct(data_root):
            raise RuntimeError("File structure does not match expected directory structure.")
        logger.info("File structure is correct.")
        logger.info("Lens startup succeeded.")
