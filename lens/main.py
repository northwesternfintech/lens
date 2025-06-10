import argparse
from pathlib import Path
from typing import Any

from loguru import logger

from lens.core import Lens


def parse_arguments() -> Any:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, required=False)

    args = parser.parse_args()
    return args


@logger.catch
def main(data_root: Path | None) -> None:
    ln = Lens()
    logger.info("Starting lens initialization check.")
    ln.startup(data_root)


if __name__ == "__main__":
    args = parse_arguments()
    specified_root = args.directory
    if specified_root is not None:
        specified_root = Path(specified_root)
    main(specified_root)
