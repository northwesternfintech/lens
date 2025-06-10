import pytest

from lens.core import Lens
from lens.test.common import TEST_DATA_PATH


def test_core_startup_metadata() -> None:
    ln = Lens()
    ln._startup_check_metadata(TEST_DATA_PATH)


def test_core_startup_file_structure() -> None:
    ln = Lens()
    ln._startup_check_files(TEST_DATA_PATH)


def test_core_startup_trade_load() -> None:
    ln = Lens()
    ln._force_startup_unsafe(TEST_DATA_PATH)
    df = ln.load_trades_for_day("avax", "2025-02-21")
    assert df.shape[1] == 5


def test_core_startup_trade_load_invalid_symbol() -> None:
    ln = Lens()
    ln._force_startup_unsafe(TEST_DATA_PATH)
    with pytest.raises(RuntimeError):
        ln.load_trades_for_day("avaxnop", "2025-02-21")


def test_core_startup_trade_load_nonexistent_date() -> None:
    ln = Lens()
    ln._force_startup_unsafe(TEST_DATA_PATH)
    with pytest.raises(RuntimeError):
        ln.load_trades_for_day("avax", "2025-02-28")


def test_core_startup_depth() -> None:
    ln = Lens()
    ln._force_startup_unsafe(TEST_DATA_PATH)
    ln.load_depth_for_day("avax", "2025-02-21")


def test_core_startup_depth_load_invalid_symbol() -> None:
    ln = Lens()
    ln._force_startup_unsafe(TEST_DATA_PATH)
    with pytest.raises(RuntimeError):
        ln.load_trades_for_day("avaxnop", "2025-02-21")


#
def test_core_startup_depth_load_nonexistent_date() -> None:
    ln = Lens()
    ln._force_startup_unsafe(TEST_DATA_PATH)
    with pytest.raises(RuntimeError):
        ln.load_trades_for_day("avax", "2025-02-28")
