from src.reports_generator.PreAction.PreAction import PreAction
from src.reports_generator.Resource import Resource
from typing import Dict
from pandas import Series


class Index(PreAction):
    def __init__(self, action_struct):
        self.tags = action_struct["tag"]
        self.resources = action_struct["resources"]

    def run(self, resources_dict: Dict[str, Resource]) -> Dict[str, Resource]:
        for resource_name, tag in zip(self.resources, self.tags):
            resource = resources_dict[resource_name]
            resource.df.insert(loc=0, column=tag, value=list(range(1, len(resource.df) + 1)))
            resources_dict[resource.name] = resource
        return resources_dict