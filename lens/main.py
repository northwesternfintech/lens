from loguru import logger

from lens.core import Lens


@logger.catch
def main():
    ln = Lens()
    logger.info("Starting lens initialization check.")
    ln.startup()


if __name__ == "__main__":
    main()
