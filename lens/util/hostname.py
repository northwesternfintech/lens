from socket import gethostname

ALLOWED_HOSTNAMES = ["black", "scholes"]


def get_hostname() -> str:
    return gethostname()


def check_valid_lens_hostaname() -> bool:
    return get_hostname() in ALLOWED_HOSTNAMES
