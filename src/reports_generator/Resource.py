from src.reports_generator import Report, config
from pathlib import Path
import json
class Resource(Report):
    def __init__(self, resource_path: str = None, file_path: str = None):
        if resource_path is None:
            raise IOError("What type of resource do you want?")
        resource_path = Path(resource_path)
        with resource_path.open('r', encoding='utf-8') as f:
            resource_struct = json.loads(f.read())
        if any([name not in resource_struct.keys() for name in config.RESOURCE_MUST_HAVE]):
            raise IOError("Not a valid resource!")
        self.prompt = resource_struct["Prompt"]
        self.needed_columns = resource_struct["Columns"]
        super().__init__(resource_struct["Name"], df_to_create_from=None, file_path=file_path)
        self.name = resource_struct["Name"]
        self.hebrew_name = resource_struct["Hebrew_Name"]

