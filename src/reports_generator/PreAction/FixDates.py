from src.reports_generator.PreAction.PreAction import PreAction
from src.reports_generator.Resource import Resource
from typing import Dict
from pandas import Series, DataFrame
from datetime import datetime


class FixDates(PreAction):

    def __init__(self, pre_action_struct):
        self.resources = pre_action_struct["resources"]
        self.columns = pre_action_struct["columns"]

    def run(self, resources_dict: Dict[str, Resource]) -> Dict[str, Resource]:
        for resource_name in self.resources:
            resource = resources_dict[resource_name]
            for column in self.columns:
                resource.df[column] = resource.df[column].apply(self.__fix_date)
            resources_dict[resource_name] = resource
        return resources_dict

    def __fix_date(self, date):
        if not isinstance(date, datetime):
            return date
        else:
            return str(date.date()).replace('-', '/')
