from src.reports_generator.PreAction.PreAction import PreAction
from src.reports_generator.Resource import Resource
from typing import Dict
from pandas import Series, DataFrame


class RemoveChars(PreAction):
    def __init__(self, pre_action_struct):
        self.resources = pre_action_struct["resources"]
        self.chars_to_strip = pre_action_struct["chars"]

    def run(self, resources: Dict[str, Resource]) -> Dict[str, Resource]:
        for resource_name in self.resources:
            resource = resources[resource_name]
            resource.df = self.__strip_chars_and_update_df(resource.df)
            resources[resource_name] = resource
        return resources

    def __strip_chars_and_update_df(self, df):
        df.rename(columns=self.__strip_chars, inplace=True)
        for col in df.columns:
            df[col] = df[col].apply(self.__strip_chars)
        return df

    def __strip_chars(self, string_to_strip):
        if not isinstance(string_to_strip, str):
            return string_to_strip
        last_stripped = ""
        while not last_stripped == string_to_strip:
            last_stripped = string_to_strip
            for char in self.chars_to_strip:
                string_to_strip = string_to_strip.strip(char)
        return string_to_strip
