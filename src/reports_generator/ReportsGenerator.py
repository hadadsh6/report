import json
import os

import pandas as pd
from pandas import DataFrame
import time
from src.reports_generator import PreAction, Action, Take, Resource, Map, Filter, Index, RemoveChars, FixDates
from typing import List, Dict, Any
from pathlib import Path

# import src.reports_generator.resources as resources

valid_actions = {"take": Take, "map": Map}  # , "search": Search]
valid_pre_actions = {"filter": Filter, "index": Index, "remove_chars": RemoveChars, "fix_dates": FixDates}


class ReportsGenerator:
    def __init__(self, report_json_path: str = None, resources: List[Resource] = None):
        self.report: Dict[str, Any] = {}
        self.actions: List[Action] = []
        self.pre_actions: List[PreAction] = []
        self.report_df: DataFrame = DataFrame()
        self.resources: Dict[str, DataFrame] = {}
        self.reports_dir = Path(os.path.dirname(__file__)).joinpath("reports")
        self.resources_dir = Path(os.path.dirname(__file__)).joinpath("resources")

        if report_json_path is None:
            raise IOError("What kind off report did you want to create?")

        print(os.getcwd())
        report_json_path: Path = Path(report_json_path)
        with report_json_path.open('rb') as f:
            report_json = json.loads(f.read())

        if resources is None:
            resources = []
            for resource_json, resource_excel_path in report_json["Resources"].items():
                resource_path = Path(self.resources_dir).joinpath(resource_json + ".json")
                if resource_excel_path == "None":
                    resource_excel_path = None
                resources.append(Resource(resource_path=resource_path, file_path=resource_excel_path))

        for resource in resources:
            resource.df.fillna('N/A')
            self.resources[resource.name] = resource

        self.validify_report_json(report_json)
        self.tags = []
        for action in self.actions:
            self.tags += action.tag


    def validify_report_json(self, report_json):
        for action_json in report_json["Actions"]:
            if action_json["Name"] not in valid_actions:
                raise IOError(f"Not a valid action name! {action_json['Name']} is not valid!")
            action = valid_actions[action_json["Name"]]
            self.actions.append(action(action_json["Args"], self.resources))
        for pre_action_json in report_json["PreActions"]:
            if pre_action_json["Name"] not in valid_pre_actions:
                raise IOError(f"Not a valid action name! {action_json['Name']} is not valid!")
            pre_action = valid_pre_actions[pre_action_json["Name"]]
            self.pre_actions.append(pre_action(pre_action_json["Args"]))

    def run_pre_actions(self):
        for pre_action in self.pre_actions:
            self.resources = pre_action.run(self.resources)

    def run_actions(self):
        for action in self.actions:
            self.report = action.run(self.report)

    def create_report_excel(self, results_path: Path = None) -> None:
        """

        :return:
        """
        self.run_pre_actions()
        self.run_actions()
        self.report_df = DataFrame(self.report)

        results_path = ReportsGenerator.get_path_to_put_results_in(results_path)
        self.report_df.to_excel(results_path)
        print(f"Successfully created results summary on: {results_path}")

    @staticmethod
    def get_path_to_put_results_in(folder_path: Path = None) -> Path:
        if folder_path is None:
            folder_path = input(
                "Please enter path to put summary excel on: (Example: C:\\Users\\USER\\Documents) \n>>")
            folder_path = folder_path.strip('"')
            folder_path = Path(folder_path)
        if not folder_path.exists():
            raise IOError("Folder doesn't exist!")
        if not folder_path.is_dir():
            raise IOError("Path isn't a folder!!")
        return folder_path.joinpath(Path(f"summary{time.asctime().replace(':', '_').replace(' ', '_')}.xlsx"))
