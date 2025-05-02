from lens.util.hostname import check_valid_lens_hostname


class Lens:
    def __init__(self):
        pass

    def startup(self):
        if not check_valid_lens_hostname():
            raise RuntimeError("Cannot start lens on invalid host.")
