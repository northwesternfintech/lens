from socket import gethostname

ALLOWED_HOSTNAMES = ["black", "scholes"]


def get_hostname() -> str:
    return gethostname()


def check_valid_lens_hostname(hostname: str) -> bool:
    return hostname in ALLOWED_HOSTNAMES
