from lens.util.hostname import check_valid_lens_hostname, get_hostname


def test_get_hostname_returns() -> None:
    assert get_hostname() is not None


def test_valid_lens_hostnames() -> None:
    assert check_valid_lens_hostname("black") is True
    assert check_valid_lens_hostname("scholes") is True


def test_invalid_lens_hostnames() -> None:
    assert check_valid_lens_hostname("nuft") is False
    assert check_valid_lens_hostname("sthn") is False
