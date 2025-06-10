from pathlib import Path

from loguru import logger

METADATA_FILENAME = "metadata.json"

TRADE_DIRNAME = "trades"
DEPTH_DIRNAME = "depth"


def check_metadata_exists(base_path: Path) -> bool:
    return base_path.joinpath(METADATA_FILENAME).exists()


def check_file_structure_correct(base_path: Path) -> bool:
    result = True
    coin_paths = [child for child in base_path.iterdir() if child.is_dir()]

    for coin_path in coin_paths:
        trade_path = coin_path.joinpath(TRADE_DIRNAME)
        depth_path = coin_path.joinpath(DEPTH_DIRNAME)
        if not trade_path.exists() or not depth_path.exists():
            logger.warning(f"Could not find all paths ({trade_path} and {depth_path}) for coin in dir {coin_path}.")
            result = False

    return result
