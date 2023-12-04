from src.reports_generator import Report
from pathlib import Path
class Resource(Report):
    def __init__(self, path: Path = None ):
        if path is None:
            raise IOError("What type of resource do you want?")
