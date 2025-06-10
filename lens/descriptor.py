from dataclasses import dataclass
from pathlib import Path

TRADE_DIRNAME = "trades"
DEPTH_DIRNAME = "depth"


@dataclass
class DataPathContainer:
    trade_paths: list[Path]
    depth_paths: list[Path]


@dataclass
class DataDescriptor:
    root: Path
    data_paths: dict[str, DataPathContainer]


def load_data_descriptor(base_path: Path) -> DataDescriptor:
    data_paths = {}
    coin_paths = [child for child in base_path.iterdir() if child.is_dir()]

    for coin_path in coin_paths:
        trade_path = coin_path / TRADE_DIRNAME
        depth_path = coin_path / DEPTH_DIRNAME
        trade_files = [child for child in trade_path.iterdir()]
        depth_files = [child for child in depth_path.iterdir()]
        data_paths[coin_path.name] = DataPathContainer(trade_files, depth_files)

    return DataDescriptor(base_path, data_paths)
