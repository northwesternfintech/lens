from lens.util.hostname import check_valid_lens_hostname, get_hostname


def test_get_hostname_returns_in_ci() -> None:
    assert get_hostname() is not None


def test_ci_hostname_not_valid() -> None:
    assert check_valid_lens_hostname() is False
