from lens.util.hostname import check_valid_lens_hostname


class Lens:
    def __init__(self) -> None:
        pass

    def startup(self) -> None:
        if not check_valid_lens_hostname():
            raise RuntimeError("Cannot start lens on invalid host.")
