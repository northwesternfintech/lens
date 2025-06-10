import argparse
from pathlib import Path
from typing import Any

from loguru import logger

from lens.core import Lens


def parse_arguments() -> Any:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, required=True)

    args = parser.parse_args()
    return args


@logger.catch
def main(data_root: Path) -> None:
    ln = Lens()
    logger.info("Starting lens initialization check.")
    ln.startup(data_root)


if __name__ == "__main__":
    args = parse_arguments()
    data_root = Path(args.directory)
    main(data_root)
