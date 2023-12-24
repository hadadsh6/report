from typing import Dict
from src.reports_generator.Resource import Resource
from src.reports_generator.Actions import Action
from abc import abstractmethod

class PreAction(Action):
    @abstractmethod
    def run(self, resources: Dict[str, Resource]) -> Dict[str, Resource]:
        raise NotImplementedError
