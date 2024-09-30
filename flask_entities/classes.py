from dataclasses import dataclass


@dataclass
class Alerts:
    success: str = None
    error: str = None