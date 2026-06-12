import subprocess


def ping_host(ip: str):
    """
    Returns a fake 'latency' value (1) if host is reachable,
    or None if unreachable / IP missing.

    Code is written for Windows (uses 'ping -n 1').
    """
    if not ip:
        return None

    try:
        result = subprocess.run(
            ["ping", "-n", "1", ip],  # Windows ping, 1 packet
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            # We don't really need exact latency, just True/False
            return 1
        else:
            return None
    except Exception:
        return None
