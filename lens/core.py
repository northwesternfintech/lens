from pathlib import Path

import pandas as pd
from loguru import logger

from lens.descriptor import DataDescriptor, load_data_descriptor
from lens.util.hostname import check_valid_lens_hostname, get_hostname
from lens.util.paths import check_file_structure_correct, check_metadata_exists, check_metadata_version_match


class Lens:
    def __init__(self) -> None:
        self.started = False
        self.descriptor: DataDescriptor

    def startup(self, data_root: Path) -> None:
        self._startup_check_hostname()
        self._startup_check_metadata(data_root)
        self._startup_check_files(data_root)
        logger.info("Lens startup succeeded.")
        self.started = True
        self.descriptor = load_data_descriptor(data_root)

    def load_trades_for_day(self, coin: str, date: str) -> pd.DataFrame:
        self._ensure_started()
        if not self._check_coin_available(coin):
            raise RuntimeError("Coin is not available in this dataset.")
        for file in self.descriptor.data_paths[coin].trade_paths:
            if date + ".csv" == file.name:
                return pd.read_csv(file, sep="|")
        raise RuntimeError("Failed to find requested date.")

    def load_depth_for_day(self, coin: str, date: str) -> pd.DataFrame:
        self._ensure_started()
        if not self._check_coin_available(coin):
            raise RuntimeError("Coin is not available in this dataset.")
        for file in self.descriptor.data_paths[coin].depth_paths:
            if date + ".csv" == file.name:
                return pd.read_csv(file, sep='|')
        raise RuntimeError("Failed to find requested date.")

    def _check_coin_available(self, coin: str) -> bool:
        return coin in self.descriptor.data_paths.keys()

    def _ensure_started(self) -> None:
        if not self.started:
            raise RuntimeError("This operation requires lens to be started before calling.")

    def _startup_check_hostname(self) -> None:
        if not check_valid_lens_hostname(get_hostname()):
            raise RuntimeError("Cannot start lens on invalid host.")
        logger.info("Host check succeeded.")

    def _startup_check_metadata(self, data_root: Path) -> None:
        if not check_metadata_exists(data_root):
            raise RuntimeError("Failed to find metadata.json file in the data directory.")
        logger.info("Metadata found.")
        if not check_metadata_version_match(data_root):
            raise RuntimeError("Metadata version does not match current version!")
        logger.info("Metadata versions match.")

    def _startup_check_files(self, data_root: Path) -> None:
        if not check_file_structure_correct(data_root):
            raise RuntimeError("File structure does not match expected directory structure.")
        logger.info("File structure is correct.")


    def _force_startup_unsafe(self, data_root: Path) -> None:
        self.started = True
        self.descriptor = load_data_descriptor(data_root)
